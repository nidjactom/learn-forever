#!/usr/bin/perl

use 5.010;
use strict;
use warnings;

sub addobj {
	my $class=shift;
	return bless{},$class;
}

my $newobj = addobj("Phill");
say $newobj;