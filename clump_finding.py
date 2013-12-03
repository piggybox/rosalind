# Clump Finding

import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k, l, t = map(int, str(lines[1]).strip().split())

pattern_frequency = {}

for j in range(len(text) - k + 1):
    pattern = text[j: j + k]
    if not pattern in pattern_frequency:
        position = []
        for i in range(len(text) - k + 1):
            if text[i:i + k] == pattern:
                position.append(i)
        pattern_frequency[pattern] = position

for k in pattern_frequency.keys():
    if len(pattern_frequency[k]) >= t:
        print k,
