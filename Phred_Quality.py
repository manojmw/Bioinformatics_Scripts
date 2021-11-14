#!/usr/bin/python

###Converting phred33 ASCII encoded quality into Quality score###
phred33 = input("Please enter the Phred+33 ASCII encoded quality:")
def PHRED2Q(phred33):
    return ord(phred33) - 33

print("The Quality score is:", PHRED2Q(phred33))

###Converting quality score of reads to phred33 values encoding letters - ASCII for a FASTQ file###
Q = int(input("Please enter the quality score:"))
def Q2PHRED(Q):
    return chr(Q + 33)

print("The Phred+33 ASCII encoded quality is:", Q2PHRED(Q))
