from Bio.Seq import translate
f = open ('rosalind_ptra.txt','r')
filecontent = f.read()
string = filecontent.split('\n')
print string[0]
print "\n"
print string[1]
i = 1
while i<=15:
	if i == 7 or i == 8:
		pass;
	else:
		output = translate(string[0], table=i, to_stop=True)
	if output == string[1]:
		print i
		i = 16
	else:
		i = i + 1