my @a=(15,25,35);
my @b=(60, 80, 90);
my @c=(36, 37, 38);

my @arr;
@arr=(\@a,\@b,\@c);

print "@arr\n";

print "All elements\n";

foreach $element (@arr)
{
	print "@$element\n";
}

print "First element each row is\n";

foreach $element (@arr)
{
	print "$element->[0]\n";
}

print "First row of first Element\n";
print "$arr[0]->[0]\n";

print "last row Last element\n";
print "$arr[-1]->[-1]\n";
