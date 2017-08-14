my $num=0;

#if num is defined do nothing,
#if num is not defined int to 10

unless(defined($num))
{
 $num=10;
}
print "value of num = $num\n";