#Frequent Words with Mismatches and Reverse Complements

import sys
import itertools as it

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k = int(lines[1].strip())
d = int(lines[2].strip())


freq = {}

patterns = map("".join, it.product("ATCG", repeat=k))
dna_mapping = {'A':'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for pattern in patterns:
    rc_pattern = ""
    for i in range(len(pattern)):
        rc_pattern += dna_mapping[pattern[-i-1]]
        
    for i in range(len(text) - k + 1):
        mismatch, rc_mismatch = 0, 0
        
        for j in range(k):
            if pattern[j] != text[i+j]:
                mismatch += 1
                if mismatch > d:
                    break

        for j in range(k):
            if rc_pattern[j] != text[i+j]:
                rc_mismatch += 1
                if rc_mismatch > d:
                    break
        
        if mismatch <= d:
            if freq.has_key(pattern):
                freq[pattern] += 1  
            else:
                freq[pattern] = 1

        if rc_mismatch <= d:
            if freq.has_key(pattern):
                freq[pattern] += 1  
            else:
                freq[pattern] = 1


max_freq = max(freq.values())

for k in freq.keys():
    if freq[k] == max_freq:
        print k,




