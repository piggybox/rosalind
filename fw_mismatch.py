# Frequent Words with Mismatches

import sys
import itertools as it

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k = int(lines[1].strip())
d = int(lines[2].strip())


freq = {}

patterns = map("".join, it.product("ATCG", repeat=k))

for pattern in patterns:
    for i in range(len(text) - k + 1):
        mismatch = 0

        for j in range(k):
            if pattern[j] != text[i + j]:
                mismatch += 1
                if mismatch > d:
                    break

        if mismatch <= d:
            if pattern in freq:
                freq[pattern] += 1
            else:
                freq[pattern] = 1

max_freq = max(freq.values())

for k in freq.keys():
    if freq[k] == max_freq:
        print k,
