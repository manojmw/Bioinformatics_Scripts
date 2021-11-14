#!/usr/bin/perl -w

#Perl program to print the genetic code for the user input amino acid

#Prompting the user to enter the amino acid
print "Please enter the name of the amino acid : \n";
chomp($amino = <STDIN>);
$amino = lc($amino);

#Printing the genetic code for the amino acid
if($amino eq 'methionine' || $amino eq 'm' || $amino eq 'met') {
    print "The genetic code for the given amino acid Methionine is : \n", "ATG", "\n";
} elsif($amino eq 'phenylalanine' || $amino eq 'f' || $amino eq 'phe') {
    print "The genetic code for the given amino acid Phenylalanine is : \n", "TTT\n", "TTC\n";
} elsif($amino eq 'leucine' || $amino eq 'l' || $amino eq 'leu') {
    print "The genetic code for the given amino acid Leucine : \n", "TTA\n", "TTG\n", "CTT\n", "CTC\n", "CTA\n","CTG\n";
} elsif($amino eq 'serine' || $amino eq 's' || $amino eq 'ser') {
    print "The genetic code for the given amino acid Serine is : \n", "TCT\n", "TCC\n", "TCA\n", "TCG\n", "AGT\n","AGC\n";
} elsif($amino eq 'tyrosine' || $amino eq 'y' || $amino eq 'tyr') {
    print "The genetic code for the given amino acid is : \n", "TAT\n", "TAC\n";
} elsif($amino eq 'arginine' || $amino eq 'r' || $amino eq 'arg') {
    print "The genetic code for the given amino acid Arginine is : \n", "CGT\n", "CGC\n", "CGA\n", "CGG\n", "AGA\n","AGG\n";
} elsif($amino eq 'alanine' || $amino eq 'a' || $amino eq 'ala') {
    print "The genetic code for the given amino acid Alanine is : \n", "GCT\n", "GCC\n", "GCA\n", "GCG\n";
} elsif($amino eq 'valine' || $amino eq 'v' || $amino eq 'val') {
    print "The genetic code for the given amino acid Valine is : \n", "GTT\n", "GTC\n", "GTA\n", "GTG\n";
} elsif($amino eq 'asparagine' || $amino eq 'n' || $amino eq 'asn') {
    print "The genetic code for the given amino acid Asparagine is : \n", "AAT\n", "AAC\n";
} elsif($amino eq 'aspartic acid' || $amino eq 'd' || $amino eq 'asp' || $amino eq 'aspartate') {
    print "The genetic code for the given amino acid Aspartic acid is : \n", "GAT\n", "GAC\n";
} elsif($amino eq 'gluatmic acid' || $amino eq 'e' || $amino eq 'glu' || $amino eq 'glutamate') {
    print "The genetic code for the given amino acid Gluatmic acid is : \n", "GAA\n", "GAG\n";
} elsif($amino eq 'glutamine' || $amino eq 'q' || $amino eq 'gln') {
    print "The genetic code for the given amino acid Glutamine is : \n", "CAA\n", "CAG\n";
} elsif($amino eq 'glycine' || $amino eq 'g' || $amino eq 'gly') {
    print "The genetic code for the given amino acid Glycine is : \n", "GGT\n", "GGC\n", "GGA\n", "GGG\n";
} elsif($amino eq 'histidine' || $amino eq 'h' || $amino eq 'his') {
    print "The genetic code for the given amino acid Histidine is : \n", "CAT\n", "CAC\n";
} elsif($amino eq 'isoleucine' || $amino eq 'i' || $amino eq 'ile') {
    print "The genetic code for the given amino acid Isoleucine is : \n", "ATT\n", "ATC\n", "ATA\n";
} elsif($amino eq 'lysine' || $amino eq 'k' || $amino eq 'lys') {
    print "The genetic code for the given amino acid Lysine is : \n", "AAA", "\n", "AAG", "\n";
} elsif($amino eq 'proline' || $amino eq 'p' || $amino eq 'pro') {
    print "The genetic code for the given amino acid Proline is : \n", "CCU", "\n", "CCC","\n", "CCA", "\n", "CAG", "\n";
} elsif($amino eq 'threonine' || $amino eq 't' || $amino eq 'thr') {
    print "The genetic code for the given amino acid Threonine is : \n", "ACU", "\n", "ACC","\n", "ACA", "\n", "ACG", "\n";
} elsif($amino eq 'tryptophan' || $amino eq 'w'  || $amino eq 'trp') {
    print "The genetic code for the given amino acid Tryptophan is : \n", "UGG", "\n";
} else {
    print "Please enter a valid amino acid name!!! \n";
}
exit;
