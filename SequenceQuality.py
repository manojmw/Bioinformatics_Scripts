#!/usr/bin/python

###Reading and Parsing sequence and Quality scores from a FASTQ file###

###Reference: Python for Genomic Data Science Course, part of Specialization in Genomic Data Science by Johns Hopkins University on Coursera.
###           All credits belong to the original authors.

print("This is a program to read and parse sequence and quality scores from a FASTQ file\n")
try:
    file = input("Please enter the name of the FASTQ file:")
except IOError:
    print("Cannot open the file!!!!....###Please try again###")

def READFASTQ(file):
    SEQ = ''
    QUAL = ''
    with open(file, 'r') as FHANDLE:
        while True:
            A = ''
            B = ''
            FHANDLE.readline()
            A = FHANDLE.readline().rstrip()
            FHANDLE.readline()
            B = FHANDLE.readline().rstrip()
            if len(A) == 0:
                break
            SEQ += A
            QUAL += B
    FHANDLE.close()
    return SEQ, QUAL

S, Q = READFASTQ(file)

print("Here is your Sequence:\n")
print(S)
print("\n")

print("Here is your Quality Score:\n")
print(Q)
