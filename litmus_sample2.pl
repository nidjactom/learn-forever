
sub oddNumbers {
	my $first = shift;
	my $last = shift;
	my @arr = ();
	while ($first<=$last){
		if ($first%2 != 0){
			push(@arr,$first);
		}
		$first=$first+1;
		return @arr;
	}
}
$_l = <>;
chomp($_l);
$_r = <>;
chomp($_r);
@res = oddNumbers($_l, $_r);
my $res_size = @res;
for($res_i=0; $res_i < $res_size; $res_i++) {
    print "@res[$res_i]\n";
}
