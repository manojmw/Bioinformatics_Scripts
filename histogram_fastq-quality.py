#!/usr/bin/python
import matplotlib.pyplot as plt

print("This is a program to create Histogram of the Quality Scores\n")

QS = input("Please enter the name of the file containing Phred33 equivalent ASCII Quality scores:")

def PHRED2QHIST(QS):
    Histogram = [0] * 50

    with open(QS, 'r') as fh:
        for element in fh:
            element = element.rstrip()
            for phred in element:
                Q = ord(phred) - 33
                Histogram[Q] += 1

    return Histogram

###Without Plot###
print(PHRED2QHIST(QS))

###With Plot###
FINAL = PHRED2QHIST(QS)
plt.bar(range(len(FINAL)), FINAL)
plt.show()
