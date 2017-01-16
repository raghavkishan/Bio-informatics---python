import sys                                  #USing Pairwise tool to determine the score.
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

f = open("rosalind_edta.txt",'r')                   #To extract input from the file.
inputs = f.read()
seq=inputs.strip().split('>')
inputv = []
for s in seq:
    if(s!=""):
        strings=s.split()
        part1=strings[0]
        part2=''.join(strings[1:])
        inputv.append(part2)

seq1 = inputv[0]
seq2 = inputv[1]

alignments = pairwise2.align.localxx(seq1, seq2)            #Using pairwise2 functions to determine the alignment

print(format_alignment(*alignments[0]))