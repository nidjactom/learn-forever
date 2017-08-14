#!/usr/bin/perl

use 5.010;
use strict;
use warnings;
use modules::emp;

my @emplist =();
my $addemp = addemp modules::emp(123,"Cody","Blackwell");

$emplist[0]=$addemp->{no};
$emplist[1]=$addemp->{fn};
$emplist[2]=$addemp->{ln};

$addemp = addemp modules::emp(456,"Raj","Chawanda");


$emplist[3]=$addemp->{no};
$emplist[4]=$addemp->{fn};
$emplist[5]=$addemp->{ln};

say "Employess";
foreach (@emplist){
	say "$_";
}
#use Data::Dumper;
#say Dumper(\$addemp);