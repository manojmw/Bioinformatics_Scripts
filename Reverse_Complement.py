#!/usr/bin/python

###Getting the reverse complement of the query DNA sequence
###Reference: Python for Genomic Data Science Course, part of Specialization in Genomic Data Science by Johns Hopkins University on [Coursera]###

####METHOD - 1####
DNA = input("Please enter the DNA sequence:")

#Defining the reverse_string function
def reverse_string(DNA):
    """This funcion reverses the DNA sequence"""
    return DNA[::-1]

#Defining the complement function
def complement(DNA):
    """This function returns the complement of the given sequence"""
    DNA = DNA.upper()
    Base_Complement = {"A":"T", "C":"G", "G":"C", "T":"A", "N":"N"} ###Creating a dictionary: Key and Value pairs
    Individual_Bases = list(DNA)
    Individual_Bases = [Base_Complement[i] for i in Individual_Bases]
    return ''.join(Individual_Bases)


#Defining the function to find the reverse complement
def ReverseComplement(DNA):
    """This function returns the reverse complement of the given DNA sequence"""
    DNA = reverse_string(DNA)
    DNA = complement(DNA)
    return DNA

print("The Reverse complement of the given DNA sequence:\n", ReverseComplement(DNA))

###METHOD - 2####

####Finding the reverse complement###
DNA = input("Please enter the DNA sequence:")
def revcomplement(DNA):
    DNA = DNA.upper()
    complement = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    rev = ''
    for base in DNA:
        rev = complement[base] + rev ###Adding rev at the end reverses the string###
    return rev

print("Reverse complement is:\n", revcomplement(DNA))
