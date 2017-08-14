print "Your name:\n";
chomp($name=<STDIN>);
if ($name =~ /^[a-z]+\s[a-z]+\s[a-z]+$/i)
{
	print "valid\n";
}
else
{
	print "invalid\n";
}