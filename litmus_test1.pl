use warnings;
use strict;
fizzBuzz(15);
sub fizzBuzz{
	my $i = shift;
	my $num = 1;
	while ($num<=$i){
		if ($num%3 == 0 and $num%5 == 0){
			print "FizzBuzz\n";
		}
		elsif ($num%3 == 0){
			print "Fizz\n";
		}
		elsif ($num%5 == 0){
			print "Buzz\n";
		}
		else{
			print "$num\n";
		}
		$num = $num+1;
	}
}
