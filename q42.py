from StringIO import StringIO                       # Using StringIO and Bio to compute tree and distance.
from Bio import Phylo

f = open("rosalind_nkew.txt","r")                           #extracting the input from the file & splitting them based on newlines.
iv = []
for i in f.read().strip().split('\n\n'):
    iv.append(i.split('\n'))
#print iv

for stringt, taxa in iv:
    i, j = taxa.split()
    #print i,j
    utree = Phylo.read(StringIO(stringt), 'newick')                    #constructing a tree using Phylo.read
    #print tree
    print (int(utree.distance(i, j))),