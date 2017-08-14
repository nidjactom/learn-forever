$a='arun';
$b='manu';
$c='ajith';
$d='amit';

print "$a $b $c $d\n";

foreach  $element($a, $b, $c, $d)
{
	$uc1=uc(substr($element,0,1));
	$uc2=uc(substr($element,-1));
	substr($element,0,1)=$uc1;
	substr($element,-1)=$uc2;
}
	
print "$a $b $c $d\n";