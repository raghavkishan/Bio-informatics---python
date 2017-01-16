from Bio import SeqIO               #To Use"Seq" in "Bio", importing "Bio"

f = open("rosalind_tfsq.txt","r+")          #taking input from a file.
SeqIO.convert(f, 'fastq', 'result', 'fasta')        # Using "SeqIO.convert" to convert it from 'fastq' to 'fasta'.
fw = open("result","r")                         #Reding the o/p and printing the same.
output = fw.read()
print output