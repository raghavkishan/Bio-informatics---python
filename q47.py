import sys
from Bio import pairwise2                       #Using pairwise2 biopython to determine the result.
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matrix

matscores = matrix.pam250

f = open("rosalind_loca.txt",'r')                   #To extract input from the file
inputs1 = f.read()
#print inputs
seq=inputs1.strip().split('>')
inputv = []
for s in seq:
    if(s!=""):
        strings=s.split()
        part1=strings[0]
        part2=''.join(strings[1:])
        inputv.append(part2)

result = []
for i in pairwise2.align.localds(inputv[0], inputv[1], matscores, -5, -5):      # To determine the score as per the given requirements using pairwise2
    print (format_alignment(*i))