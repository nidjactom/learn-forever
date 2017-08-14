my @nums=(76,45,68,15,123,97,53,36,84);
@nums=sort(@nums);
# @nums=sort{$a<=>$b} @nums;
print "@nums\n";
print "@nums[0..4]\n";
# print "@nums[($#nums-3)..$#nums]\n";
print "@nums[-4..-1]\n";