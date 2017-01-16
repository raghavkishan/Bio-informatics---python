from Bio.Seq import Seq                         #Using Biopython to find reverse complement.
from Bio.Alphabet import generic_dna

f = open("rosalind_revp.txt",'r')                   #To extract input from the file
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
string =  inputv[0]
#print string

result = []
position1 = []
position2 = []

#print len(string)

for j in range(4, 13):                      #Determing the palindrome sequences in the given input
    for i in range(0, len(string)-j+1):
        #print string[i:i+j]
        s = string[i:i + j]
        my_dna = Seq(s,generic_dna)
        if my_dna == my_dna.reverse_complement():
            position1.append(i+1)
            position2.append(j)
            result.append(my_dna)


#print result
for i in range(len(position1)):             #printing the output in the specifed format.
    print position1[i],position2[i]