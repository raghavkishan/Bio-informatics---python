import urllib2
import re

def calc(resopnse):
    string1 = response.read().splitlines()      #formatting the for the input
    #print string1
    string2 = ''
    for i in range(1,len(string1)):
        string2 +=string1[i]
    #print string2
    val = ([m.start() for m in re.finditer('(?=N[^P][ST][^P])',string2)]) # determining the locations of the strings identified by the regular expression.
    for i in range(len(val)):
        val[i]+=1
    return val

f = open ("rosalind_mprt.txt",'r')
input = f.readlines()
num_lines = sum(1 for line in open("rosalind_mprt.txt"))
for i in range(0,num_lines):
    response = urllib2.urlopen('http://www.uniprot.org/uniprot/'+input[i].rstrip()+'.fasta')   # acccessing the input.
    val = calc(response)
    if val!=[]:                         # formatting the output.
        print
        print input[i].rstrip()
        for j in val:
            print j,
