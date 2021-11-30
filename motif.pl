#!/usr/bin/perl -w

#Prompting the user to enter the name of the file containing the protein data
print "Please enter the name of the file containing the sequence : \n";
chomp($file = <STDIN>);

#Opening the file and associating the file with a file handler[i.e., prothandler] and if unable to open the file, printing an error message
unless(open(PROTHANDLER, $file))
{
  print STDERR "Unable to open the file '$file' \n";
  print "Please try again!!!\n";
  exit;
}

#Reading the protien data and storing it in a variable called @protein
@protein = <PROTHANDLER>;

#Closing the file
close(PROTHANDLER);

#Motifs are easy to search in a single string than searching in different lines
#We will join all the characters and lines using the 'join' function including line breaks
$protein = join('', @protein);

#removing whitespaces if any so as to make it one continuous string
$protein =~ s/\s//g;

#Using Do-Until Loop
#Doing (Prompting the user to enter the MOTIF sequence, searching for the motif and printing the results;)
#a set of tasks until a specific condition (exiting the do-until loop when there is no user input) is satisfied
do
{
      #Prompting the user to enter the motif sequence
      print "Please enter the MOTIF sequence : \n";
      chomp($motif = <STDIN>);
      $motif = uc($motif);

      if ($protein =~ /$motif/)
      {
        print "The given pattern was found in the sequence file!!!! \n \n";
      }
      else
      {
        print "#####Ooops! Could not find the given patterne in the sequence file#### \n \n";
      }
} until($motif =~ /^\s*$/);

#Number of occurences and Position
#Calculatin the GC content from a DNA $file
#Subroutine to read FASTA files
#Subroutine - Area and Melting temperature

exit;
