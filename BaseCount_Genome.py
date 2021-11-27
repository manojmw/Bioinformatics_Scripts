#!/usr/bin/python

###Reading and Counting the frequency of each base in a Genome using the Python COLLECTIONS module###

###Reference: Python for Genomic Data Science Course, part of Specialization in Genomic Data Science by Johns Hopkins University on [Coursera]###

import collections

try:
    file = input("Please enter the file name:")
except IOError:
    print("Cannot open the file...Please try again!!!")

def readgenome(file):
    genome = ''
    with open(file, 'r') as GHANDLE:
        for line in GHANDLE:
            if not line[0] == '>':
                line = line.rstrip()
                genome += line
    return genome
    GHANDLE.close()

sequence = readgenome(file)
print(collections.Counter(sequence))
