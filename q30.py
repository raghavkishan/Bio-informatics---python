from numpy import zeros

f = open("rosalind_edit.txt",'r')                   #input from file
seq = f.read().split(">")            #extracting the strings from the input.
#print seq
inputv = []
for s in seq:
    if(s!=""):
        strings=s.split()
        part1=strings[0]
        part2=''.join(strings[1:])
        inputv.append(part2)
#print inputv
lenc = len(inputv[0])+1
lenr = len(inputv[1])+1
str1 = inputv[0]
str2 = inputv[1]

mat = zeros((lenr,lenc),dtype=int)      #creating a matrix of the order of lengths of the input string.
#print mat
for i in range(1,lenc):
    mat[0][i] = i
#print mat
for i in range(1,lenr):
    mat[i][0] = i
#print mat

for i in range(1,lenr):             #To determine the edit distance.
    for j in range(1,lenc):
        if str2[i-1] != str1[j-1]:
            mat[i,j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1] + 1)
        else:
            mat[i][j] = mat[i-1][j-1]

#print mat
print mat[-1][-1]                   #printing the edit diatance.




