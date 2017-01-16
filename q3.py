f = open('rosalind_dna.txt','r');
string =  f.read();
print string.count('A');
print string.count('C');
print string.count('G');
print string.count('T');