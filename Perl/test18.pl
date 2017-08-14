sub compare_arrays
{
	my $first=$_[0];
	my $second=$_[1];
	
	print "@$first\n";
	print "@$second\n";
}

my @nums=(10, 20, 30);
my @data=(40,50,60,70,80);
compare_arrays(\@nums, \@data);