D = {'A':4,'R':6,'N':2,'D':2,'C':2,'Q':2,'E':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,'S':6,'T':4,'W':1,'Y':2,'V':4,'STOP':3};
f = open ('rosalind_mrna.txt','r');
string  = f.readline().strip();
value = 1;
i = 0;
length = len(string);
while ( i < length):
	value = value * D[string[i]];
	i = i + 1;
value = value * 3;
value = value % 1000000;
print value;