#!/usr/bin/python

###Matching READS from a FASTQ file to a GENOME###

###Reference: Algorithms for DNA Sequencing Course, part of Specialization in Genomic Data Science by Johns Hopkins University on [Coursera]###

print("This is a program to match READS from a FASTQ file to a GENOME\n")

###Extracing SEQUENCE from a GENOME###
try:
    file = input("Please enter the file name of the GENOME:")
except IOError:
    print("Cannot open the file...Please try again!!!")
print("\n")

def READGENOME(file):
    SEQUENCE = ''
    with open(file, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            if not line[0] == '>':
                SEQUENCE += line
    return SEQUENCE

Genome = READGENOME(file)

####Extracing READS from FASTQ file###
try:
    file = input("Please enter the name of the FASTQ file containing READS:")
except IOError:
    print("Cannot open the file!!!!....###Please try again###")

def READFASTQ(file):
    SEQUENCE = []
    with open(file, 'r') as FASTQHANDLE:
        while True:
            A = ''
            FASTQHANDLE.readline()
            A = FASTQHANDLE.readline().rstrip()
            FASTQHANDLE.readline()
            FASTQHANDLE.readline()
            if len(A) == 0:
                break
            SEQUENCE.append(A)
    FASTQHANDLE.close()
    return SEQUENCE

Reads = READFASTQ(file)

###NAIVE Algorithm for matching READS###
def NAIVE(P, T): ###'P' is the pattern to search for and 'T' is the text in which the pattern is to be searched###
    occurrences = []
    for i in range(len(T) - len(P) + 1): ###Reason being it gives us every position of 'P' in T but we do not run past                                 ##the length of 'T'
        match = True                     ###Boolean variable initializing as True###
        for j in range(len(P)):
            if not T[i+j] == P[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

numberMatches = 0
for read in Reads:
    match = NAIVE(read, Genome)
    if len(match) > 0:
        numberMatches += 1

print("%d of %d reads matched the Genome" % (numberMatches, len(Reads)))
