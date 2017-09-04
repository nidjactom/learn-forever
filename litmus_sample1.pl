use warnings;
use strict;
my @arr=(5,1,2,3,4,5);
findNumber(\@arr, 1);
sub findNumber {
    my $array_ref = shift;
    my @test = @$array_ref;
    my $k = shift;
    foreach (@test) {
        if ($_ == $k){
            print "found";
            return 'YES';
        }
    }
    print"not found";
    return 'NO';
}
if A[0] = b
