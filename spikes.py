from Bio import SeqIO 

for dna in SeqIO.parse("sequences.fasta", "fasta"):
	print ("Loading ...")
	if "s protein" in str(dna.description).lower() or "spike" in str(dna.description).lower() or "surface" in str(dna.description).lower():
		with open ("D:/Bioinformatics/Proteomics/sessions/Session 9 9-8-2020/spike for sars cov 2/Spike.fasta", "a") as f:
			f.write(f">{dna.description}\n{dna.seq}\n")
print("Done")

