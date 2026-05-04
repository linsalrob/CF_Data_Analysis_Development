import gzip
import sys
from Bio import SeqIO

gb = sys.argv[1]
gff = sys.argv[2]

print(f"Convert genbank: {gb} to gff {gff}", file=sys.stderr)

with gzip.open(gb, "rt") as handle, open(gff, "w") as out:
    out.write("##gff-version 3\n")
    for record in SeqIO.parse(handle, "genbank"):
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

            out.write(
                f"{record.id}\tGenBank\t{feature.type}\t{start}\t{end}\t.\t{strand}\t.\t{';'.join(attrs)}\n"
            )
