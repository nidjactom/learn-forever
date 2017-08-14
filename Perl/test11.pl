
my @arr=(10,20,30,40,50,60,70.80);

my @chars=qw(a b c d);

print "@arr\n";

#insert 3-arg should be 0
#replace 3-arg should how many to replace

splice(@arr,3,0,@chars);

print "@arr\n";