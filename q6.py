f = open('rosalind_gc.txt','r');
l = f.readlines();
list1 = [];
d = {};
for a in l:						# to strip '\n' from the list elements contaning.
	a = a.strip();
	list1.append(a);
index = ''
for i in list1:
		if 'Rosalind' in i:
			index = i
			d[index] = ''
		else:
			d[index] += i
#print d;
maxkey = d.keys()[0]
maxvalue =  d.values()[0]
maxg = maxvalue.count('G')
maxc = maxvalue.count('C')
length = len(maxvalue)
maxcount = (float((maxc+maxg)/float(length))*100)
finalkey = '';
finalvalue = '';
finalcount = 0; 
vc = 0;
for key,value in d.iteritems():
	vc = (float((value.count('C')+value.count('G'))/float(len(value)))*100);
	if vc > maxcount:
		maxkey = key;
		maxvalue = value;
		maxcount = vc;

print maxkey.strip('>')
print round(maxcount,7)