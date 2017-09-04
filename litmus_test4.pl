use warnings;
use strict;
my $_date_size = 0;
$_date_size = <>;
my @_dates;
while (@_dates < $_date_size){
	my $_dates_temp = <>;
	chomp($_dates_temp);
	push @_dates, $_dates_temp;
}
my @testarray = reformatDate(\@_dates);
my $datesize = @testarray;
print ("size = $datesize \n Test => @testarray\n");
sub reformatDate{
	my $arr_ref = shift;
	print $arr_ref;
	my @arr = @$arr_ref;
	my $i = 0;
	my $num = @arr;
	my @datearray = ();
	my %Mon = (
		"jan" => '01',
		"feb" => '02',
		"mar" => '03',
		"apr" => '04',
		"may" => '05',
		"jun" => '06',
		"jul" => '07',
		"aug" => '08',
		"sep" => '09',
		"oct" => '10',
		"nov" => '11',
		"dec" => '12',
		);
	while ($i < $num){
		my @parts = split(' ',$arr[$i]);
		my $year = $parts[2];
		my $month = $Mon{lc($parts[1])};
		my @datestring = split('th',$parts[0]);
		my $date = $datestring[0];
		if (length($date) == 1){
			$date = '0' . $date;
		}
		my $completedate = $year . '-' . $month . '-' . $date;
		push(@datearray,"$completedate");
		$i = $i + 1;
	}
	return @datearray;
}
