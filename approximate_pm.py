# Approximate Pattern Matching

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
pattern = str(lines[0]).strip()
text = str(lines[1]).strip()
d = int(lines[2].strip())


 
for i in range(len(text) - len(pattern) + 1):
	mismatch = 0
	for j in range(len(pattern)):
		if pattern[j] != text[i+j]:
			mismatch += 1
	if mismatch <= d:
		print i,





