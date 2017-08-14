# use List::MoreUtils qw(zip);

# my @alpha=('a'..'z');
# my @num=(1..26);
# %table=zip(@alpha,@num);

my %table;
@table('a'..'z')=(1..26);

print "Enter any alphabets:\n";

chomp($value=lc(<STDIN>));
my @arr=split(//,$value);

foreach (@arr)
{
	print "$_ => $table{$_}\n";
}