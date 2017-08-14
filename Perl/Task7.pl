my @array;
my $i;
print "Input is:\n";
for($i=0;$i<=5;$i++)
{
	chomp($temp=<STDIN>);
	push (@array,$temp);
}

# @part1=@array[0..($#array/2)];
# @part2=@array[(($#array/2))..$#array];

@part1=splice(@array,0,($#array/2)+1);
@part2=@array;


@part1=reverse(@part1);
@part2=sort{$a<=>$b} @part2;

@res = (@part1,@part2);

print "Output is:\n";
foreach (@res)
{
	print $_, "\n";
}
