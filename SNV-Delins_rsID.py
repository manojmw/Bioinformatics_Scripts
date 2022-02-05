#!/usr/bin/python

####This is a python program to extract the rs_ID and SNV's or DELINS from the SNP_file####

###Written by: Manoj M Wagle
###Date: 6 January, 2021
###Email: [manoj.wagle@learner.manipal.edu]
###Department: Department of Bioinformatics, Manipal School of Life Sciences, Manipal, MAHE, Karnataka, India - 576104

#Importing the python regular expression(re) module
import re

print("This is a program to extract the RS_ID's and Single-nucleotide Variant(SNV) or Deletion-Insertion(DELINS) from the file(containing the SNP's)!!!\n")
print("You can also redirect this program's output to a file that will be saved in your current working directory!\n(Example: 'python3 SNV-Del_rsid.py > output.txt')\n")

#Prompting the user to enter the file name, opening and reading('r') the file
SNP_file = open(input("Please enter the name of the file containg the rs_ID's:\n"), 'r')

for line in SNP_file:
    line = line.rstrip() #removes any trailing characters at the end of a string
    rs_ID = re.findall('[\d]+. rs[\d]+',line) #matching the rs id's
    SNV = re.findall('^SNV:.+', line) #matching the SNV's
    Deletions = re.findall('^DELINS:.+', line) #matching the DELINS

#Printing the matched characters
    if len(rs_ID)>0:
        print(rs_ID)
    if len(SNV)>0:
        print(SNV,"\n")
    if len(Deletions)>0:
        print(Deletions,"\n")

#Closing the file
SNP_file.close()
