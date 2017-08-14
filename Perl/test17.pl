my $num1=10;
my $num2=54;
my $res= myfun($num1, $num2);
print "Result=$res\n";

sub myfun
{
		my $res=$_[0] + $_[1];
		# return $res;
	}