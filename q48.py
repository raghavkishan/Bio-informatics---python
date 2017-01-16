import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matrix

matscores = matrix.blosum62

f = open("rosalind_edta.txt",'r')                   #To extract input from the file
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

for i in pairwise2.align.localds(inputv[0], inputv[1], matscores, -11, -1):         #Determining the final result. i.e. score and strings.
    print (format_alignment(*i))