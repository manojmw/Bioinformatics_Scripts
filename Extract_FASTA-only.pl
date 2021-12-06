#!/usr/bin/perl -w

use strict;
use warnings;

print "\nThis is a program to extract and display only the sequence from a FASTA file\n\n";
print "Please enter the name of the file : \n";
chomp(my $user = <>);

#Subroutine to extract FASTA sequence data from a file
sub EXTRACT_FASTA
{
    my($file) = @_;

    unless(open(FASTAHANDLER, $user))
    {
      print STDERR "Cannot open file '$user'\n";
      print "Please try again!!!\n";
      exit;
    }

    my @data = <FASTAHANDLER>;
    close FASTAHANDLER;

    #Initializing the variables
    my $sequence = ' ';

    foreach my $line(@data)
    {
        #removing blank lines
        if ($line =~ /^\s*$/)
        {
            next;
        }
        #Removing any comments
        elsif ($line =~ /^\s*#/)
        {
            next;
        }
        #Removing header from FASTA file
        elsif ($line =~ /^>/)
        {
            next
        }
        else
        {
            $sequence .= $line;
        }

    }
    #Removing any white spaces present in the sequence data
    $sequence =~ s/\s//g;
    print $sequence,"\n";

}
#Calling Subroutine
EXTRACT_FASTA($user);
