from itertools import product
f = open ('rosalind_lexf.txt','r')
input = f.readlines()
string = input[0].split()
n = input[1]
list1 = list(product(string,repeat = int(n)))
string  = (map(''.join,list1))
print string
string.sort()
for i in string:
    print i

