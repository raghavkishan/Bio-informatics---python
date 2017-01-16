import urllib2
import re

def calc(resopnse):
    string1 = response.read().splitlines()      #formatting the for the input
    string2 = ''
    for i in range(0,len(string1)):
        string2 +=string1[i]
    #print string2
    val = (re.findall('(GO\; GO\:\d{7}\; P\:.+?;)',string2)) #identifying all the biological processes in which the protein is involved.
    return val

def format(val):                                #To format the obtained strings from calc(response).
    string2 = ''
    for i in range(0, len(val)):
        string2 += val[i]
    value = re.findall('(P\:.+?;)',string2)
    result1 = [w.replace('P:','') for w in value]
    result = [w.replace(';', '') for w in result1]
    return result

f = open ("rosalind_dbpr.txt",'r')
input = f.readlines()
num_lines = sum(1 for line in open("rosalind_dbpr.txt"))
for i in range(0,num_lines):
    response = urllib2.urlopen('http://www.uniprot.org/uniprot/'+input[i].rstrip()+'.txt')   # acccessing the input.
    val = calc(response)
    #print val
    value = format(val)                 #printing the ouput.
    for i in value:
            print i
