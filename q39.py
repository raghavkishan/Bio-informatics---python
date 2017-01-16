import sys
import re

f = open('rosalind_nwck.txt', 'r')                                                  #Extracting the input from a file.
pairs = [l2.split('\n') for l2 in f.read().strip().split('\n\n')]           #First: Spliting the data to components and then
for tr, leaves in pairs:                                                    #For each pair of tree and nodes.
    leaves = leaves.split()
    symbols = iter(re.split('([(),])', tr))                                 #splitting based on special characters and itertaing using an iterator object.
    while next(symbols) not in leaves:
        pass
    c1 = 0                                                                  #C1 & c2 are counts for climbing and descending the tree.
    c2 = 0
    for i in symbols:                                                       #Using specific symbols to determine if the value is to be addded or subtracted to c1 & c2.
        if i in leaves:
            break
        if i in ',)':
            if c2 > 0:
                c2 -= 1
            else:
                c1 += 1
        if i in ',(':
            c2 += 1
    print c1 + c2                                                           # printing the final distance between the symbols.

