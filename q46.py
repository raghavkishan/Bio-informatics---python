from numpy import log, exp
f = open("rosalind_eval.txt","r")
inputv = f.read().strip().split('\n')
n = int(inputv[0])
string = inputv[1]
y = inputv[2]
gcinputs = y.split(" ")
#print gcinputs

for i in gcinputs:
    gccount = float(i)
    gcount = string.count("G")
    acount = string.count("A")
    ccount = string.count("C")
    tcount = string.count("T")
    z = log(gccount/2)*(gcount+ccount) + log((1-gccount)/2)*(acount+tcount)
    print round(exp(z)*(n-1),3),

#refrence : Peer discussion