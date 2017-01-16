f = open ('test1.txt','r')
string = f.read()
#print string;
lstring = string.splitlines()
string1 = lstring[0]
string2 = lstring[1]
vstring = string2.split(' ')
sequencesize = int(vstring[0])
Limit = int(vstring[1])
checker = int(vstring[2])
i = 0;
k = 0;
finallist=[];
while (i < len(string1) - Limit + 1):
	stringofL = string1[i:i+Limit];
	#print stringofL
	d = {}
	j = 0;
	while (j < len(stringofL) - sequencesize + 1):
		if stringofL[j:j+sequencesize] not in d:
			d[stringofL[j:j+sequencesize]] = 0
		d[stringofL[j:j+sequencesize]] = d[stringofL[j:j+sequencesize]] + 1;
		#print stringofL[j:j+sequencesize]
		j = j+1
	for k,v in d.iteritems():
		#print k,v;
		if d[k] >= checker:
			if k not in finallist:
				finallist.append(k)
	i = i + 1

outfinalstr = ''
for i in finallist:
	outfinalstr = outfinalstr + i + ' '
print outfinalstr