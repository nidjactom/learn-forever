$str='sample data was added using editor';
$str =~ tr/[aeiou]/[AEIOU]/;
print $str, "\n";