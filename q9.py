D = {'UUU':'F',
'UUC':'F',
'UUA':'L',
'UUG':'L',
'UCU':'S',
'UCC':'S',
'UCA':'S',
'UCG':'S',
'UAU':'Y',
'UAC':'Y',
'UAA':'Stop',
'UAG':'Stop',
'UGU':'C',
'UGC':'C',
'UGA':'Stop',
'UGG':'W',
'CUU':'L',
'CUC':'L',
'CUA':'L',
'CUG':'L',
'CCU':'P',
'CCC':'P',
'CCA':'P',
'CCG':'P',
'CAU':'H',
'CAC':'H',
'CAA':'Q',
'CAG':'Q',
'CGU':'R',
'CGC':'R',
'CGA':'R',
'CGG':'R',
'AUU':'I',
'AUC':'I',
'AUA':'I',
'AUG':'M',
'ACU':'T',
'ACC':'T',
'ACA':'T',
'ACG':'T',
'AAU':'N',
'AAC':'N',
'AAA':'K',
'AAG':'K',
'AGU':'S',
'AGC':'S',
'AGA':'R',
'AGG':'R',
'GUU':'V',
'GUC':'V',
'GUA':'V',
'GUG':'V',
'GCU':'A',
'GCC':'A',
'GCA':'A',
'GCG':'A',
'GAU':'D',
'GAC':'D',
'GAA':'E',
'GAG':'E',
'GGU':'G',
'GGC':'G',
'GGA':'G',
'GGG':'G'};
f = open ('rosalind_prot.txt','r');
string = f.read();
slength = len(string);
i = 0;
fstring = '';
flag = 1;
while ( flag ):
        s = string[i:i+3]
       	if D[s] == 'Stop':
                flag = 0;
	else:
		fstring = fstring+D[s];
        i = i + 3;
print fstring;