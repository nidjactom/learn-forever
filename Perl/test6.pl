@names=qw(chethan hari mahesha ram ja);

#sort these names based on the length of the string

@names=sort { length($b) <=> length($a)} @names;

foreach (@names)
{
	print "$_\n";
}