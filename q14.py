from itertools import product
f = open('rosalind_kmer.txt','r')
l = f.readlines()
s = ''

string = []                     # to strip '\n' from the list elements contaning.or use rstrip()
d = {}
for a in l:
	a = a.strip()
	string.append(a)
for i in range(1,len(string)):
    s = s + string[i]
print s

list1 = list(product('TAGC',repeat = 4))        #to create the cartesian product of TAGC
stringcp  = (map(''.join,list1))
stringcp.sort()
print stringcp

stringlist = []
for i in range(0,len(s)-3):
    stringlist.append(s[i:i+4])
print stringlist

d= {}
for i in stringcp:
    d[i]=stringlist.count(i)

for key,value in sorted(d.items()):
        print value,








