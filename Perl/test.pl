sub fun
{
	my $num = 'LOCAL VARIABLE';
	print "IN Sub = $num\n";
	print "IN Sub = $main::num\n";
	
}
our $num=10;
my $name;
print "Enter your name:";
$name=<STDIN>;
print "Programe being executed = $0\n";
print "Programs PID = $$\n";
print "User input was = $name";
print "Package name = ",__PACKAGE__,"\n";
print "num value =", $num, "\n";
print "num value = $main::num\n";
#print "num value = ", eval('$'.__PACKAGE__.'::num'. "\n";
&fun();