print "Input Date:\n";
chomp($input=<STDIN>);
if ($input =~ /^\d{1,2}([\/-])\d{1,2}\1\d{4}$/)
{
	print "Valid Date Format\n";
}
else
{
	print "InValid Date Format\n";
}