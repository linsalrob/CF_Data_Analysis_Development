"""
A library to read and provide data for the worldwide samples that we have processed.

"""

import os
import sys
import argparse

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

def read_worldwide_taxonomy(sample, taxonomy='family', all_taxa=False, raw=False, verbose=False):
    """
    Read the taxonomy file for a sample and return a data frame.
    :param sample: sample name
    :param taxonomy: level of taxonomy to read (default is 'family')
    :param all_taxa: read all taxa, not just bacteria
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
    df = df[~df['taxonomy'].str.endswith(f'{taxonomy[0]}__')]
    df = df.set_index('taxonomy')
    df.index = df.index.str.replace(f'{taxonomy[0]}__', '').str.replace('Candidatus ', '')
    df.index = df.index.str.split(';').str[-1]

    df = df.sort_index(axis=1)
    return df

def read_worldwide_subsystems(sample, level="subsystems", normalisation='norm_ss', verbose=False):
    """
    Read the subsystems file for a sample and return a data frame.
    :param sample: sample name
    :param level: level of subsystems to read (default is 'subsystems')
    :param normalisation: One of ['norm_ss', 'norm_all', 'raw']. norm_ss (default) is normalised on the number of reads that are in subsystems, norm_all is normalised on the total number of reads, and raw is the raw data.
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

    return df