#!/usr/bin/python

###Checking if the query DNA sequence contains STOP codon

###Reference: Python for Genomic Data Science Course, part of Specialization in Genomic Data Science by Johns Hopkins University on Coursera.
###           All credits belong to the original authors.

DNA = input("Please enter the DNA sequence:")

#Defining the function to identify stop codon
def STOP_CODON(DNA, frame = 0):
    "This is a fucntion to check if the given DNA sequence has a STOP codon!"
    Found_Stop_codon = False
    Stop_Codons = ("TAA", "TAG","TGA")
    for i in range(frame,len(DNA),3):
        codon = DNA[i:i+3].upper()
        if codon in Stop_Codons:
            Found_Stop_codon = True
            break
    return Found_Stop_codon

if(STOP_CODON(DNA)):
    print("The given DNA sequence CONTAINS in-frame STOP codon")
else:
    print("The given DNA sequence DOES NOT CONTAIN in-frame STOP codon")
