# Pattern Matching

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
pattern = str(lines[0]).strip()
text = str(lines[1]).strip()

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        print i,
