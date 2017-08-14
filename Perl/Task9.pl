print "Input:\n";
chomp($input=<STDIN>);
if ($input =~ /^\d+$/)
{
	print "Integer\n";
}
elsif ($input =~ /^[a-z].*/i)
{
	print "String\n";
}
elsif ($input =~ /^\d+\.\d+$/)
{
	print "Float\n";
}
else
{
	print "Others\n";
}