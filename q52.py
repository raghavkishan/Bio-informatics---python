from Bio.Seq import Seq
from itertools import chain
f = open('test1.txt', 'r')
s = f.read().strip().split('\n')
srv = []
for i in s:  # determining the revese complement.
    a = Seq(i)
    srv.append("%s"%a.reverse_complement())

ssrv = list(set(s + srv))  # Add the reverse complement of each string.

flatten = lambda stringlist: chain.from_iterable(stringlist)
l = len(ssrv[0])
for i in range(l - 1, 1, -1):
    string1 = dict(flatten([[(d[j:j + i],d[j + 1:j + i + 1]) for j in range(l - i)] for d in ssrv]))  # Determine  a list of the (n-i)mers where i iterates towards 0 until the string is obtained.
    string2 = next(iter(string1))                               #Using two variables to determine its value and check for exit condition.
    string3 = string2
    result = ''                                                    #Holds the final result.
    while True:
        if string3 in string1:
            result = result + string3[-1]
            string3 = string1.pop(string3)
            if string3 == string2:
                print result                                    #Displaying the final result.
        else: break

