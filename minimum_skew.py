# Minimum Skew

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()

gc = 0  # g - c
skew = []


for i in range(len(text)):
    if text[i] == 'C':
        gc -= 1
    if text[i] == 'G':
        gc += 1
    skew.append(gc)


m = min(skew)
for i in range(len(skew)):
    if skew[i] == m:
        print i + 1,
