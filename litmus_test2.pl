use warnings;
use strict;
lastletters('APPLE');
sub lastletters{
	my $word = shift;
	my $last = substr($word,-1);
	my $secondlast = substr($word,-2, 1);
	print "$last $secondlast";
	return;
}
