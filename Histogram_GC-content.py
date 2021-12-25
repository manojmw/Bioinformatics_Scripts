#!/usr/bin/python

###Reference: Specialization in Genomic Data Science by Johns Hopkins University on [Coursera]###

###Importing modules
import matplotlib.pyplot as plt

print("This is a program to plot the GC content of the sequence from a FASTQ file\n")

try:
    file = input("Please enter the name of the file:")
except IOError:
    print("Cannot open the file...Please try again!!!")

def READFASTQ(file):
    SEQUENCE = []
    with open(file, 'r') as FASTQHANDLE:
        while True:
            A = ''
            FASTQHANDLE.readline()
            A = FASTQHANDLE.readline().rstrip()
            FASTQHANDLE.readline()
            FASTQHANDLE.readline().rstrip()
            if len(A) == 0:
                break
            SEQUENCE.append(A)
    FASTQHANDLE.close()
    return SEQUENCE

reads = READFASTQ(file)

def GCHIST(reads):
    GC = [0] * 100      ###GC will store the number of GC bases at each position###
                        ###All the reads are of length 100 in the given FASTQ file###
    total = [0] * 100   ###Keeping track of total bases###

    for read in reads:
        read = read.rstrip()
        for base in range(len(read)):
            if read[base] == 'C' or read[base] == 'G':
                GC[base] += 1
            total[base] += 1

    for base in range(len(GC)):
        if total[base] > 0:
            GC[base] /= float(total[base])
    return GC

FINAL = GCHIST(reads)
print(FINAL)

plt.plot(range(len(FINAL)), FINAL) ###Line plot###
plt.show()
