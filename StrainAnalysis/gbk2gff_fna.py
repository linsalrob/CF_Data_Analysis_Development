import gzip
import sys
import binascii
import argparse
from Bio import SeqIO


def is_gzip_file(f):
    """
    Is this a gzip file?
    :param f: the file to test
    :return: True if the file is gzip compressed else false
    """
    with open(f, 'rb') as i:
        return binascii.hexlify(i.read(2)) == b'1f8b'

def convert(gb, gff, fna):
    opener = open
    if is_gzip_file(gb):
        opener=gzip.open

    with opener(gb, "rt") as handle, gzip.open(gff, "wt") as gffout, gzip.open(fna, 'wt') as fnaout:
        gffout.write("##gff-version 3\n")
        for record in SeqIO.parse(handle, "genbank"):
            fnaout.write(f">{record.id} {record.description}\n{record.seq}")
            for feature in record.features:
                if feature.type not in {"CDS", "gene", "rRNA", "tRNA", "tmRNA", "ncRNA"}:
                    continue

                start = int(feature.location.start) + 1
                end = int(feature.location.end)
                strand = "+" if feature.location.strand == 1 else "-" if feature.location.strand == -1 else "."
                q = feature.qualifiers

                attrs = []
                for key in ["locus_tag", "gene", "product", "protein_id"]:
                    if key in q:
                        attrs.append(f"{key}={q[key][0].replace(';', ',')}")
                if not attrs:
                    attrs.append("ID=unknown")

                gffout.write(
                    f"{record.id}\tGenBank\t{feature.type}\t{start}\t{end}\t.\t{strand}\t.\t{';'.join(attrs)}\n"
                )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert gzip Genbank file to GFF and FNA')
    parser.add_argument('-i', '--input', help='input genbank file', required=True)
    parser.add_argument('-f', '--fasta', help='fasta file to write')
    parser.add_argument('-g', '--gff3', help='gff3 file to write')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    

    faf = None
    gff = None
    if args.fasta:
        faf = args.fasta
    else:
        faf = args.input
        if '.gbff' in faf:
            faf = faf.replace('.gbff', '.fna')
        elif '.gbk' in faf:
            faf = faf.replace('.gbk', '.fna')
        else:
            faf += '.fna'
    if not faf.endswith('.gz'):
        faf += '.gz'


    if args.gff3:
        gff = args.gff3
    else:
        gff = args.input
        if '.gbff' in gff:
            gff = gff.replace('.gbff', '.gff')
        elif '.gbk' in gff:
            gff = gff.replace('.gbk', '.gff')
        else:
            gff += '.gff'
    if not gff.endswith('.gz'):
        gff += '.gz'

    print(f"Converting {args.input} to gff3: {gff} and fasta: {faf}", file=sys.stderr)
    convert(args.input, gff, faf)


        


