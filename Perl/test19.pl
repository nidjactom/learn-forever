open (TEXT, "data.txt") or die ("$!");
my @arr = <TEXT>;
close (TEXT);

print "@arr\n";