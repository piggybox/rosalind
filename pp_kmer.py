# Find a Profile-most probable k-mer in a string.
# Input: A string Text, an integer k, and a k × 4 matrix Profile.
# Output: A Profile-most probable k-mer in Text.

import sys
from operator import mul

lines = open(sys.argv[1].strip(), 'r').readlines()
dna = lines[0].strip()
k = int(lines[1])
profile = [map(float, l.split(" ")) for l in lines[3:]]


def calculate_probablity(kmer):
    t = []
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            t.append(profile[i][0])
        elif kmer[i] == 'C':
            t.append(profile[i][1])
        elif kmer[i] == 'G':
            t.append(profile[i][2])
        elif kmer[i] == 'T':
            t.append(profile[i][3])
    return reduce(mul, t, 1)


best_pattern = ""
best_probability = 0.0000
for i in range(len(dna) - k + 1):
    kmer = dna[i:i+k]
    # print kmer, calculate_probablity(kmer)
    if calculate_probablity(kmer) > best_probability:
        best_pattern = kmer
        best_probability = calculate_probablity(kmer)

print best_pattern

