#!/usr/bin/perl

use 5.010;
use strict;
use warnings;

my $directory= "D:/Perl";

opendir (my $dir, $directory) or die $!;

while(my $list=readdir($dir)) {
	say "$list";	
}

closedir($dir);