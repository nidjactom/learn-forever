open (TEXT, "data.txt") or die ("$!");
my @arr = <TEXT>;
close (TEXT);

open (LOGFILE, ">>out.txt") or die ("$!");
foreach $element(@arr)
{
	if($element=~/^a.*[lt]$/i)
	{
		print LOGFILE $element;
	}
}
close(LOGFILE);