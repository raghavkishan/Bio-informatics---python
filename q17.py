 import math
f = open('rosalind_prob.txt','r')                           #reading the input from a file
input = f.readlines();
string = input[0]
GCcontents = (input[1].split(' '))                  #splitting the contents into elemnts of a list
GCcontents = [float(i) for i in GCcontents]         #converting strings into float values.
probabilities = []
#print GCcontents
print string

GC = string.count('G') + string.count('C')          #Calculating count of GC
AT = string.count('A') + string.count('T')          #Calculating count of AT

def probability(GCcontent):                         #Calculating probability
    ATcontent =  1- GCcontent
    a = GCcontent/2
    b = ATcontent/2
    result = math.pow(a,GC) * math.pow(b,AT)
    returnvalue = math.log10(result)
    return round(returnvalue,3)

for i in GCcontents:                                #printing probability
    print probability(i)