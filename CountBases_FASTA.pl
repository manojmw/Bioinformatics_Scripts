#!/usr/bin/perl -w

use strict;
use warnings;

###Written by: Manoj M Wagle
###Date: 06 December, 2020
###Email: [manoj.wagle@learner.manipal.edu]
###Department: Department of Bioinformatics, Manipal School of Life Sciences, Manipal, MAHE, Karnataka, India - 576104

###Perl script to count the nucleotide bases in a FASTA file###

print "Please enter the name of the FASTA file : \n";
chomp(my $user = <>);

# Subroutine to extract FASTA sequence data from a file
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

    return($sequence);
}


#Subroutine for counting nucleotide bases
sub count_base
{
  my $DNA = EXTRACT_FASTA($user);
  $DNA = uc($DNA);
  my @DNA = split//, $DNA;

  #Initializing the varaibles
  my $A_count = 0;
  my $C_count = 0;
  my $G_count = 0;
  my $T_count = 0;
  my $errors = 0;

  foreach my $base(@DNA)
  {
    if($base eq 'A')
    {
      $A_count++;
    }
    elsif($base eq 'C')
    {
      $C_count++;
    }
    elsif($base eq 'G')
    {
      $G_count++;
    }
    elsif($base eq 'T')
    {
      $T_count++;
    }
    else
    {
      $errors++;
    }

  }
  print "-----------------------------\n";
  print "Count of each nucleotide base\n";
  print "-----------------------------\n";
  print "Adenine = $A_count\n\n", "Cytosine = $C_count\n\n", "Guanine = $G_count\n\n", "Thymine = $T_count\n\n", "Non-bases = $errors\n\n";

}

count_base();
