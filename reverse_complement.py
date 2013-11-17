# Reverse Complement

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()

result = ""
dna_mapping = {'A':'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for i in range(len(text)):
	result += dna_mapping[text[-i-1]]

print(result)