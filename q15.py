f = open('rosalind_fib.txt', 'r')              #To open and read the file
input = f.read()
inputs = input.split(' ')               #To Assign split the content based on space and assign it to a list
n = int(inputs[0])
k = int(inputs[1])
print n,k
def rabbitcount(n, k):                  #The deifinition of rabbitcount gives the final population as the end of n months
    if n == 1 or n == 2:
        return 1
    else:
        return rabbitcount(n - 1, k) + (k * rabbitcount((n - 2), k))

print rabbitcount(n, k)
