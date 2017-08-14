print ("Enter the value:");
$value=<STDIN>;
chomp($value);

$pal=scalar reverse($value);

if (lc($value) eq lc($pal))
{
	print "PALINDROME \n";
}
else
{
	print "NOT PALINDROME\n";
}