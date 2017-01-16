from Bio.Seq import translate
from Bio.Seq import Seq
f = open ('rosalind_orf.txt','r')
filecontent = f.readlines()
s = filecontent[1]
#print s
string3 = Seq(s)                                #to find the reverse complement of a string.
stringrc = str(string3.reverse_complement())

location  = []                                  #to find the start codons in the string
for i in range(0,len(s)):
    if i+2>=len(s):
        print "i+2>length(string)"
        break
    if s[i] == 'A' and s[i + 1] == 'T' and s[i + 2] == 'G':
        string = s[i:i+3]
        #print string
        location.append(i)
#print location

list = []
for k in location:
    seq = s[k:]
    list.append(translate(seq,table = 1,to_stop = False))
#print list

locationrc = []                                 #to find the start codons in the reverse complement of the string
for i in range(0,len(stringrc)):
    if i+2>=len(stringrc):
        print "i+2>length(string)"
        break
    if stringrc[i] == 'A' and stringrc[i + 1] == 'T' and stringrc[i + 2] == 'G':
        string = s[i:i+3]
        # print string
        locationrc.append(i)
#print locationrc

listrc=[]
for k in locationrc:
    seq = stringrc[k:]
    listrc.append(translate(seq,table = 1,to_stop = False))
#print listrc

l = list+listrc
#print l
l1=[]
d={}

for i in l:                                        # to identify strings containing stop codon
    if '*' in i:
        l1.append(i[:i.find('*')])
#print l1

for i in l1:                                       # to remove items suplicate strings
    d[i]=''
for key in d.iterkeys():
    print key