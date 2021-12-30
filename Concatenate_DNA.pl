#!/usr/bin/perl -w

###Perl script showing concatenation of DNA sequence by 3 different methods###

###Written by: Manoj M Wagle
###Date: 13 November, 2020
###Email: [manoj.wagle@learner.manipal.edu]
###Department: Department of Bioinformatics, Manipal School of Life Sciences, Manipal, MAHE, Karnataka, India - 576104

print "Please enter the first DNA sequence:\n";
chomp($DNA1 = <STDIN>);
print "Please enter the second DNA sequence:\n";
chomp($DNA2 = <STDIN>);

#Concatenation of the given two DNA sequences by method 1
$DNA3 = $DNA1 . $DNA2;
print "Here is the concatenation of the given DNA sequences by Method 1:","\n", $DNA3,"\n";

#Concatenation of the given two DNA sequences by method 2
$DNA4 = "$DNA1$DNA2";
print "Here is the concatenation of the given DNA sequences by Method 2:","\n", $DNA4,"\n";

#Concatenation and printing of the given DNA sequences by method 3
print "Here is the concatenation of the given DNA sequences by method 3:","\n", $DNA1, $DNA2, "\n";

exit;
