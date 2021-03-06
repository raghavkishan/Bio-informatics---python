import sys                      # reference: Biopython pairwise2
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist
matscores = matlist.blosum62

f = open("rosalind_gcon.txt",'r')                   #To extract input from the file
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


for i in pairwise2.align.globalds(inputv[0], inputv[1], matscores, -5, 0):
    print(format_alignment(*i))
