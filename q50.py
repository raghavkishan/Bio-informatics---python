f = open("rosalind_ba9j.txt","r")               #extracting the
inputv = f.read().strip()

burrows = [i for i in inputv]
sortedburrows = sorted(burrows)

def prepend(str1,str2):                 #prepending burrows to sortedburrows.
    c = [str1[k] + str2[k] for k in range(0,len(burrows))]
    return c

def prepsort(x,y):                      #performing the prepending and sorting.
    str3 = prepend(x,y)
    str3.sort()
    return str3

sortedburrows = prepsort(burrows, sortedburrows)            #determing the final result.
for i in range (0,len(burrows)-2):
    sortedburrows = prepsort(burrows, sortedburrows)

for i in range(0,len(sortedburrows)):
    if sortedburrows[i][-1] == '$':
        result = sortedburrows[i]

print result