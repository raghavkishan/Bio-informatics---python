f = open('rosalind_fibd.txt', 'r')              #To open and read the file
input = f.read()
inputs = input.split(' ')               #To Assign split the content based on space and assign it to a list
months = int(inputs[0])
age = int(inputs[1])
values = list()
i = 0
while i < months:
    if i < 2:                           #To calculate the result when the month is less than two.
        result = 1
        values.append(result)
        i += 1
    elif (i < age) or (age == 0):           #To calculate the result whern the month is less than the age of the 1st pair of rabbits or if the rabbits live for ever.
        result = values[i - 1] + values[i - 2]
        values.append(result)
        i += 1
    elif i == age:                        #To calculate the result when the month is equal to the age of the 1st pair of rabbits
        result = values[i - 1] + values[i - 2] - 1
        values.append(result)
        i += 1
    else:                               #To calculate the result when the month is greater than the age.
        result = values[i - 1] + values[i - 2] - values[i - (age + 1)]
        values.append(result)
        i += 1

print values

print result