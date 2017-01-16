f = open ('rosalind_revc.txt','r');
string =f.read();
rstring = string[::-1];
ostring = '';
D = {};
D['A'] = 'T';
D['T'] = 'A';
D['C'] = 'G';
D['G'] = 'C';
D['\n'] = '';
for i in rstring:
	ostring = ostring + D[i];
print ostring;