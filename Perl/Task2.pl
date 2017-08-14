$str='new way to do this';

$uc1=uc(substr($str,0,3));
$uc2=uc(substr($str,-4));
substr($str,0,3)=$uc1;
substr($str,-4)=$uc2;

print $str ,"\n";