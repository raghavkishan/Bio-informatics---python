f = open("rosalind_lcsm.txt",'r')
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
length = len(inputv[0])
#print length
def substring(input):
    return [input[i:j+1] for i in range(length) for j in range(length)]
list1 = filter(None,substring(inputv[0]))
#print list1
selectedstring = ''
list2 = []
list3 = []
list4 = []
for i in list1:
    for j in inputv:
        if i not in j:
            list2.append(i)
        break

list3 = list(set(list2))
#print list3
list4 = list(set(list1)-set(list3))
#print list4
for i in list4:
    if len(i)>len(selectedstring):
        selectedstring = i

print selectedstring