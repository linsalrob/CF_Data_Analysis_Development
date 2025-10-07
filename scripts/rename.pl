use strict;
use Getopt::Std;
use Data::Dumper;
use File::Temp qw/ tempfile/;
use Rob;
my $rob = new Rob;


my %rename = (
'1112926_20171212_S' => '1447437_20171212_S',
'1128691_20170206_S' => '1128691_20171206_S',
'1255498_20171212_S' => '1590009_20171212_S',
'1316979_20171215_S' => '1651490_20171215_S',
'1598281_20180508_S' => '1588281_20180508_S',
'1723809_20180227_S' => '1085876_20180227_S',
'649354_20170206_S' => '639354_20171206_S',
'652927_20180226_S' => '715927_20180226_S',
'658355_20180301_S' => '658355_20180327_S',
'777851_20170918_S' => '778851_20170918_S',
'788707_20181126_S' => '788707_20181129_S',
'698917_20190119_S' => '698917_20180119_S');

my %opts;
getopts('f:v', \%opts);
unless ($opts{f}) {
	die <<EOF;
	$0
	-f file to parse (required)
	-v verbose output
EOF
}


my ($fh, $filename) = tempfile(UNLINK=>1);
print STDERR "Writing to $filename\n";
open(IN, $opts{f}) || die "$! : $opts{f}";
my $n=0;
while (<IN>) {
	foreach my $k (keys %rename) {$n += s/$k/$rename{$k}/g}
	print $fh $_;
}
close IN;
if ($opts{v}) {print STDERR "$n changes made\n"}

unlink $opts{f} || die "Can't remove $opts{f} after renaming reads";
seek($fh, 0, 0) or die "Seek failed: $!";
open(OUT, ">$opts{f}") || die "Can't create new $opts{f}";
while (<$fh>) {print OUT}
close OUT;
close $fh;


