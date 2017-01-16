from Bio import Entrez
from Bio import SeqIO

f = open ("rosalind_frmt.txt",'r')                      #Parsing the input from the input file
input = f.read()
input1 = input.replace(" ",", ")
shorteststring = ''
Slength = 0
shorteststringdesc = ''

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=[input1], rettype="fasta")               #USing Bio.Entres module retrieving the strings associated with the  GenBank entry IDs.
records = list(SeqIO.parse(handle,"fasta"))

length = len(records)                                                   #to format and print the output appropriately.
slength = len(records[0].seq)
for i in range(1,length):
    if len(records[i].seq) < slength:
        slength = len(records[i].seq)
        shorteststring = records[i].seq
        shorteststringdesc = records[i].description

print ">"+shorteststringdesc
print shorteststring







