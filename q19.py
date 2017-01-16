f = open("rosalind_subs.txt","r")
string = f.readlines()
inputs = string[0].rstrip()
seq = string[1].rstrip()
#print inputs
#print len(inputs)
result = []
length = len(seq)

for i in range(len(inputs) - length + 1):       #calculating the positions of the substring.
    if inputs[i:i + length] == seq:
        result.append(i + 1)

for i in result:
    print i,



