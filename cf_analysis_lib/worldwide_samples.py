"""
A library to read and provide data for the worldwide samples that we have processed.

"""
import gzip
import json
import os
import sys

__author__ = 'Rob Edwards'

import pandas as pd

WORLDWIDE_ATAVIDE='../WorldWideDataAnalysis/Atavide/'

def worldwide_samples():
    """
    Read the samples from the Atavide directory and return a list of sample names.
    """
    if not os.path.exists(WORLDWIDE_ATAVIDE):
        print(f"Error: {WORLDWIDE_ATAVIDE} does not exist", file=sys.stderr)
        sys.exit(1)

    samples = [f for f in os.listdir(WORLDWIDE_ATAVIDE) if os.path.isdir(os.path.join(WORLDWIDE_ATAVIDE, f))]
    return samples

def read_worldwide_metadata(sample, drop_amplicon=False):
    """
    Read the metadata file for a sample and return a data frame.
    :param sample: the sample name
    :param drop_amplicon: if True, drop the rows where library_strategy is AMPLICON
    :return: the metadata data frame
    """

    # read the json file at WORLDWIDE_ATAVIDE/{sample}/{sample}.metadata.json.gz
    # and convert it to a data frame
    metadata_file = os.path.join(WORLDWIDE_ATAVIDE, sample, f"{sample}.metadata.json.gz")

    if not os.path.exists(metadata_file):
        print(f"Error: {metadata_file} does not exist", file=sys.stderr)
        sys.exit(1)

    with gzip.open(metadata_file, 'rt') as f:
        metadata = json.load(f)
    df = pd.DataFrame(metadata)
    df = df.set_index('run')
    if (df['library_strategy'].str.contains('AMPLICON')).any():
        if drop_amplicon:
            df = df[~df['library_strategy'].str.contains('AMPLICON')]
            if df.empty:
                print(f"Warning: No samples left after dropping amplicon data for {sample}", file=sys.stderr)
        else:
            print(f"Warning: Some samples in {sample} have library_strategy: AMPLICON, consider dropping them", file=sys.stderr)
    return df


def read_worldwide_taxonomy(sample, taxonomy='family', all_taxa=True, raw=False, verbose=False):
    """
    Read the taxonomy file for a sample and return a data frame.
    :param sample: sample name
    :param taxonomy: level of taxonomy to read (default is 'family')
    :param all_taxa: by default we read all the taxa, but if this is False we only read the bacteria
    :param raw: read the raw data. By default we read the normalised data
    :param verbose: more output
    :return: data frame with the taxonomy
    """

    taxfile = f'{sample}_{taxonomy}.norm.tsv.gz'
    if raw:
        taxfile = f'{sample}_{taxonomy}.raw.tsv.gz'

    taxonomy_file = os.path.join(WORLDWIDE_ATAVIDE, sample, "taxonomy_summary", taxfile)

    if not os.path.exists(taxonomy_file):
        print(f"Error: {taxonomy_file} does not exist", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Reading taxonomy from {taxonomy_file}", file=sys.stderr)

    df = pd.read_csv(taxonomy_file, sep='\t', compression='gzip')

    if not all_taxa:
        df = df[df['taxonomy'].str.contains('k__Bacteria')]
    # here we filter for those taxa that contain the taxonomy level we are interested in
    df = df[df['taxonomy'].str.contains(f'{taxonomy[0]}__')]
    # but not those that end with the taxonomy level
    df = df[~df['taxonomy'].str.endswith(f'{taxonomy[0]}__')]
    df['taxonomy'] = df['taxonomy'].str.replace('Candidatus ', '')
    df['taxonomy'] = df['taxonomy'].str.replace(f'{taxonomy[0]}__', '')

    df = df.set_index('taxonomy')
    df.index = df.index.str.split(';').str[-1]

    df = df.sort_index(axis=1)
    return df

def read_worldwide_subsystems(sample, level="subsystems", normalisation='norm_ss', drop_suspected_amplicon=False, verbose=False):
    """
    Read the subsystems file for a sample and return a data frame.
    :param sample: sample name
    :param level: level of subsystems to read (default is 'subsystems')
    :param normalisation: One of ['norm_ss', 'norm_all', 'raw']. norm_ss (default) is normalised on the number of reads that are in subsystems, norm_all is normalised on the total number of reads, and raw is the raw data.
    :param drop_suspected_amplicon: if True, drop the rows where the subsystems sum is 0 (these are suspected amplicon samples)
    :param verbose: more output
    :return: data frame with the subsystems
    """

    sfile = f'{sample}_{level}_{normalisation}.tsv.gz'

    subsystems_file = os.path.join(WORLDWIDE_ATAVIDE, sample, "subsystems", sfile)

    if not os.path.exists(subsystems_file):
        print(f"Error: {subsystems_file} does not exist", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Reading subsystems from {subsystems_file}", file=sys.stderr)

    df = pd.read_csv(subsystems_file, sep='\t', compression='gzip', index_col=0)

    # we drop suspected amplicon if the drop_suspected_amplicon=True flag is set. These are samples
    # where the column sum is 0 for the subsystems data
    before_dropping = df.shape
    if drop_suspected_amplicon:
        df = df.loc[:, df.sum(axis=0) != 0]
        if df.empty:
            print(f"Warning: No samples left after dropping suspected amplicon data for {sample}", file=sys.stderr)
        if verbose:
            print(f"Before dropping suspects, shape is {before_dropping} and after is {df.shape}", file=sys.stderr)

    return df


def read_worldwide_data(sample, sslevel='subsystems', ss_normalisation='norm_ss',
                        taxonomy='family', all_taxa=True, raw_taxa=False, drop_amplicon=True,
                        drop_suspected_amplicon=True, verbose=False):
    """
    Reads worldwide benchmark data by combining functional subsystems data, taxonomic abundance data,
    and available metadata. The function integrates these datasets into a unified format
    appropriate for downstream data analysis tasks.

    :param sample: Identifier for selecting a specific sample from the dataset
    :param sslevel: Granularity level of the subsystems data. Default is 'subsystems'
    :param ss_normalisation: Normalisation approach applied to the subsystems data. Default is 'norm_ss'
    :param taxonomy: Taxonomic level of interest for the study (e.g., 'family', 'genus'). Default is 'family'
    :param all_taxa: Boolean flag indicating whether to include all taxonomic classifications. Default is True
    :param raw_taxa: Boolean flag indicating whether to return raw taxonomy data without transformations. Default is False
    :param drop_amplicon: Boolean flag indicating whether to drop samples with amplicon sequencing. Default is True
    :param drop_suspected_amplicon: if True, drop the rows where the subsystems sum is 0 (these are suspected amplicon samples)
    :param verbose: Boolean flag controlling the verbosity of printed debug outputs. Default is False

    :return: A tuple containing:
        - A DataFrame combining subsystems data and taxonomic abundance data
        - A DataFrame of associated metadata
    """

    ss_df = read_worldwide_subsystems(sample, sslevel, ss_normalisation, drop_suspected_amplicon, verbose)
    ss_df = ss_df.T
    if verbose:
        print(f"Read {ss_df.shape[0]} samples and {ss_df.shape[1]} subsystems", file=sys.stderr)
    otu = read_worldwide_taxonomy(sample, taxonomy, all_taxa, raw_taxa, verbose)
    otu = otu.T
    if verbose:
        print(f"Read {otu.shape[0]} samples and {otu.shape[1]} {taxonomy}", file=sys.stderr)
    df = ss_df.merge(otu, left_index=True, right_index=True, how='inner')

    metadata = read_worldwide_metadata(sample, drop_amplicon=drop_amplicon)
    if verbose:
        print(f"Read {metadata.shape[0]} samples and {metadata.shape[1]} metadata columns", file=sys.stderr)

    # next we need to make sure that the index for metadata matches the index for the data and drop any
    # data samples that are not in the metadata
    df = df.loc[df.index.intersection(metadata.index)]

    return df, metadata
