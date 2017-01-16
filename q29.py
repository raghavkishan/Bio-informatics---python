import operator

f = open("rosalind_hamm.txt","r")           # Extracting the input from the file.
inputs = f.read().split()
#print inputs[0]
#print inputs[1]

val = map(operator.ne, inputs[0],inputs[1]).count(True)         #"map" will apply the function specified on the iterables.
print val