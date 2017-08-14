#!/usr/bin/perl
package modules::emp;
use 5.010;
use strict;
use warnings;

sub addemp {
	my $person=shift;
	my $newemp={no=>shift, fn=>shift, ln=>shift};
	bless $newemp, $person;
	return $newemp;
}

1;