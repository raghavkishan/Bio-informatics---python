f = open("rosalind_cunr.txt","r")                   #reading input from file as integer
n = int(f.read())

def doublefactorial(n):
    if n<=0:
        return 1
    return n*doublefactorial(n-2)                   #Calculating the double factorial

print (doublefactorial(2*n-5) % 1000000)                #final output