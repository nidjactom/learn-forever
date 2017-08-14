
print "File = @ARGV\n";
@arr=<>;
my $sum=0;
foreach (@arr)
{
	$sum=$sum+(split(/,/,$_))[1];
}
print "Sum = $sum\n";