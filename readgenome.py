#!/usr/bin/python

###Reading Genome from a FASTA file###
try:
    myfile = input("Please enter the file name:")
except IOError:
    print("Cannot open the file...Please try again!!!")

def readgenome(myfile):
    genome = ''
    with open(myfile, 'r') as GENOMEHANDLE:
        for line in GENOMEHANDLE:
            if not line[0] == '>':
                line = line.rstrip()
                genome += line
    return genome
    GENOMEHANDLE.close()

print("Here is your Genome Sequence:")
print(readgenome(myfile))
