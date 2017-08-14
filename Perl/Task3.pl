print ("Enter the name:");
$name=<STDIN>;
chomp($name);

$first=substr($name,0,1);
$last=substr($name,-1);

if (lc($first) eq lc($last))
{
	print "EQUAL \n";
}
else
{
	print "NOT EQUAL\n";
}