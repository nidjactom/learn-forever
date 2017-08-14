=cut
$date='sample data was added using editor';
my ($first,$last) = (split(/ /,$date))[0,-1];

print "$first\n";
print "$last\n";
=cut


@values=qw(10-20 56-23 65-12 34-76 25-45 42-38);

@values=sort{(split(/-/,$a))[-1] <=> (split(/-/,$b))[-1]} @values;

foreach (@values)
{
	print "$_\n";
}