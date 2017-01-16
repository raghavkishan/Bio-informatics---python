from math import sqrt

def restrictionmap(input):                                      #Function to determine the requires set of values

    size = int(0.5 + 0.5 * sqrt(8.0 * len(input) + 1))         # To determine the size of the output from the input. This is used in the exit condition.

    result = [0]                                                   # Final result list. it will have 0 as the first element.
    result.append(max(input))                                       #Appending max value to the result array. This will be the last element of the array.

    input.remove(result[1])                                 #Removing the max value from the given input list.
    a = set(input)                                              #'a' stores a unique set of the input list through which we can iterate.

    for i in a:
        if sum([(abs(i - j) in input) for j in result]) == len(result):         #For each element in the set as determined above,the diff between value of set and reslut is calculated and checked if it exists in the input.
            for j in result:                                                    #Then the boolean values are added to be compared with the length of the result. If true, it eneters the loop.
                input.remove(abs(i - j))                                #For every input value in the result the difference values as calulated are removed from the inputlist that add to form the max element.
            result.append(i)
            if len(result) == size: break                           #Exit condition as described above.
    return sorted(result)

if __name__ == '__main__':
    f = open("rosalind_pdpl.txt")
    inputv = f.read().strip().split()
    input = []
    for i in inputv:
        input.append(int(i))
    result  = restrictionmap(input)
    for each in result:
        print each,

#reference: As discussed with peers and class.