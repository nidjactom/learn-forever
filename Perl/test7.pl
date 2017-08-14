use List::Util qw(max min sum);

my @nums=(10,20,54,23,30,65,40,50);
$sum = sum(@nums);
$max = max(@nums);
$min = min(@nums);
print "Sum = $sum\n";
print "Max = $max\n";
print "Min = $min\n";