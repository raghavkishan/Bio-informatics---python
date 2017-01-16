def LIS(seq):           #Longest Increasing subsequence.
    list = []
    for i in range (0,n):
        j = 0
        elemupdte = False
        for j in range(0, len(list)):
            if list[j] > seq[i]:
                list.insert(j,seq[i])
                #print list
                list.pop(j+1)
                elemupdte = True
                break

        if not elemupdte:
            list.insert(j,seq[i])
    return sorted(list)

def LDS(seq):                       #Using dynamic programming to determine the longest decreasing subsequence.
    temparr = [0] * len(seq)
    lenseq = len(seq)
    for i in range(lenseq - 2, -1, -1):
        for j in range(lenseq - 1, i, -1):
            if temparr[i] <= temparr[j] and seq[i] > seq[j]:
                temparr[i] = temparr[j] + 1

    max_value = max(temparr)

    result = []
    for i in range(len(temparr)):
        if max_value == temparr[i]:
            result.append(seq[i])
            max_value -= 1

    return result

if __name__ == "__main__":

    f = open("rosalind_lgis.txt",'r')                   #To extract input from the file
    inputs = f.read().split('\n')
    #print inputsrosalind_lgis
    n = int(inputs[0])
    #print n
    seq = map(int,inputs[1].split())
    #print seq
    lis = LIS(seq)
    for i in lis:
        print i,
    print
    dis = LDS(seq)                              #Calling LDS function as define above.
    for i in dis:
        print i,

#refrence: www.hackerrank.com

