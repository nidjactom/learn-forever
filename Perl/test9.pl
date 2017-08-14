%sale=('PRN' => 5500,
	'MON' => 8500,
	'CPU' => 10500,
	'KB' => 2000);
	
	print "Type the Cost you want to check (PRN, MON, CPU, KB):";
	chomp($choice=uc(<STDIN>));
	
if(exists($sale{$choice}))
{
	print "\nCost of $choice is $sale{$choice}.\n"; 
}
else
{
print "Unknown Product\n";
}