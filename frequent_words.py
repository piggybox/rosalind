# Frequent Words

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k = int(lines[1]).strip()
l = len(text)

d = {}

for i in range(l - k + 1):
	kmer = text[i:i + k]
	if kmer in d:
		d[kmer] += 1
	else:
		d[kmer] = 1

max_frequency = max(d.values())

answer = [kmer for kmer, freq in d.items() if freq == max_frequency]
print(" ".join(answer))