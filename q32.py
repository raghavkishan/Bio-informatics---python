import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

f = open("test1.txt",'r')                   #To extract input from the file
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

#print inputv

alignments = pairwise2.align.globalms(inputv[0], inputv[1], 10, 1, -10, -1)

print(format_alignment(*alignments[0]))
