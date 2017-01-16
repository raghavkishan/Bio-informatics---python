import itertools as it

f = open("test1.txt","r")
inputv = f.read().split(" ")
print inputv
print list((it.product(inputv,repeat = 4)))

d = {}
