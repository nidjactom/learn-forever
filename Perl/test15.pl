$str='hello world 16 of perl 23i';

$str=~s/(\d+)/$1+1/ge;
print "$str\n";