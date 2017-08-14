$str='sample data was added';

substr($str,index($str, 'a'),1)='*';
substr($str,rindex($str, 'a'),1)='*';
print $str ,"\n";