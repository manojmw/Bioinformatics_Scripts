#!/usr/bin/python

###Reading Genome from a FASTA file and printing only the sequence###

try:
    myfile = input("Please enter the file name:")
except IOError:
    print("Cannot open the file...Please try again!!!")

def readgenome(myfile):
    genome = ''
    with open(myfile, 'r') as GSEQHANDLE:
        for line in GSEQHANDLE:
            if not line[0] == '>': ###Since the first line starts with '>', we will ignore this line and store only the sequence (which starts from the second line in a FASTA file).
                line = line.rstrip() ###Removing any trailing spaces
                genome += line
    return genome
    GSEQHANDLE.close()

print("Here is your Genomic Sequence: \n")
print(readgenome(myfile))
