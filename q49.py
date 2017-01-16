from collections import deque               #Using collections to rotate strings.
f = open("rosalind_ba9i.txt","r")                   #Rotating the string.
inputv = f.read().strip()

midreslist = []
midreslist.append(inputv)

def rotation(seq):                          #rotation of characters being performed.
    d = deque(seq)
    rlist = []
    for i in range(0,len(d)):
        rlist.append(''.join(map(d.rotate(-1),d)))
    return (rlist)

r = rotation(inputv)
for i in range(0,len(r)-1):
    midreslist.append(r[i])

#print midreslist

midreslist.sort()                       #sorting.

#print midreslist
result = ""

for i in range(0,len(midreslist)):          #determing the Burrows-Wheeler Transform.
    result = result + midreslist[i][-1:]

print result
