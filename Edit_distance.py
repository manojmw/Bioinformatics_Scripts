#!/usr/bin/python

###Reference: Algorithms for DNA Sequencing Course, part of Specialization in Genomic Data Science by Johns Hopkins University on [Coursera]###

###Calculating edit distance based on dynamic programming

def editDistance(x, y):
    #Create distance matrix
    D = []

    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))

    #Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = i

    #Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)

    #Edit distance is the value in the bottom right corner of the matrix
    return D[-1][-1]

###To call the above function, provide the input strings for X and Y as shown below
#x = 'ATGCGC GACT'
#y = 'ATGCGCGACTC'

###Printing the output
#print(editDistance(x,y))
