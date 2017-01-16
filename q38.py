f = open("rosalind_tree.txt","r")           #taking input from the file
inputv = f.readlines()
inputs = []
edge = []
for i in inputv:
    inputs.append(i.rstrip())

n = int(inputs[0])

for i in inputs:
    edge.append(map(int,i.split()))             #mapping the nodes.

edges = edge[1:]
countedges = len(edges)

print (n-countedges-1)