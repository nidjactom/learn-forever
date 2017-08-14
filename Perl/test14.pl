$str='hello world of perl';

$str=~s/^(\w+)(.*?)(\w+)$/$3$2$1/;

print "$str\n";