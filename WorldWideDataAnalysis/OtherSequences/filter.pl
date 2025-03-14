use strict;
use Getopt::Std;
use Data::Dumper;
use Rob;
my $rob = new Rob;

open(IN, "../cf_sputum_sra_ids.txt") || die "cf_sputum_sra_ids.txt";
my %want;
while (<IN>) {
	chomp;
	$want{$_}=1;
}
close IN;

open(IN, "pairwise_mash_distances.no16s.tsv") || die "pairwise_mash_distances.no16s.tsv?";
while(<IN>) {
	if (/From/) {print; next}
	my @a=split /\t/;
	my $print = 1;
	if ($a[0] =~ /RR/ && !$want{$a[0]}) {$print = 0}
	if ($a[1] =~ /RR/ && !$want{$a[1]}) {$print = 0}
	print if $print;
}

	# read the list of selected ids
	# srr_wanted = set()
	# with open("cf_sputum_sra_ids.txt", 'r') as f:
	#     for l in f:
	#             srr_wanted.add(l.strip())
	#             wlt = wlt[wlt.index.isin(srr_wanted)]
