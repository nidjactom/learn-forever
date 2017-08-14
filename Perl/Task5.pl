$a='arun'

foreach $element('arun','basu','chet','dine','elan')
{
	$first=substr($element,0,1);
	$last=substr($element,-1);
	print "Element = $element , First= $first , Last=$last\n";
}
	