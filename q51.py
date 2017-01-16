from Bio.Seq import Seq                 #Using Biopython to find the reverse complement.
f = open("rosalind_dbru.txt","r")               #extracting the input from a file.
inputv = f.readlines()
s = []
for i in inputv:
    s.append(i.strip())

srv = []

for i in s:                             #determining the revese complement.
    a = Seq(i)
    srv.append("%s" %a.reverse_complement())

a = []
b = []
for i in range(len(s)):
    p = s[i][:-1]
    q = s[i][1:]
    pq = (p,q)
    a.append(pq)

for i in range(len(s)):                 #Using set to determine adjcency list and to idenotify unique sets.
    r = srv[i][:-1]
    s = srv[i][1:]
    rs = (r, s)
    b.append(rs)

result = set(a)                 #Using set to identify unique sets.
result.update(b)

for (a,b) in sorted(result):            #displaying the result.
    print '(%s, %s)' %(a,b)

