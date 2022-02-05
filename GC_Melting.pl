#!/usr/bin/perl -w

###This is a perl script to calculate: the GC content(%) of the query DNA sequence and the Melting temperature (Tm)###

###Written by: Manoj M Wagle
###Date: 18 November, 2020
###Email: [manoj.wagle@learner.manipal.edu]
###Department: Department of Bioinformatics, Manipal School of Life Sciences, Manipal, MAHE, Karnataka, India - 576104

print "Please enter your sequence : \n";
$DNA = <STDIN>;
chomp($DNA);

$DNA = uc($DNA);

#Counting individual bases
$A = ($DNA =~ tr/A//);
$C = ($DNA =~ tr/C//);
$G = ($DNA =~ tr/G//);
$T = ($DNA =~ tr/T//);

#Finding the total base count of the given DNA sequence
$basecount = ($A + $G + $C + $T);
$length = length($DNA);
$nonbase = length($DNA) - $basecount;

#Finding the GC content in the given DNA sequence
$GC = (($G+$C)/$basecount) * 100;

#printing the result
print "\nHere is your given DNA sequence : \n", $DNA, "\n","\n";
print "-> The length of the given DNA sequence is :", $length, "\n","\n";
print "-> Here is the total base count of the given DNA sequence :", $basecount, "\n","\n";
print "-> The number of non-bases in the given sequence is :",$nonbase, "\n","\n";
print "-> The percentage of gc content in the given sequence is :";
printf("%.2f", $GC);
print "%\n\n";

if ($basecount<14) {
      $Tm = ($A+$T)*2 + ($C+$G) * 4;
      print "->The length of the given sequence is less than 14 nucleotides, the Melting temperature is:";
      printf("%.2f", $Tm);
      print " deg.C";
} else {
      $Tm = 64.9 +41*($G+$C-16.4)/($A+$T+$G+$C);
      print "->The length of the given sequence is greater than 14 nucleotides, the Melting temperature is: ";
      printf("%.2f", $Tm);
      print " deg.C";
}
print "\n";

exit;
