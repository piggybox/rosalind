# Frequent Words with Mismatches and Reverse Complements

import sys
import itertools

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k, d = map(int, lines[1].split())
freq = {}
# patterns = map("".join, itertools.product("ATCG", repeat=k))
dna_mapping = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def mutations(kmer, d):
    result = []
    for indices in itertools.combinations(range(len(kmer)), d):
        # all possible replacements including the original
        # in this way it will cover cases for d - 1, d - 2 ... 0
        for replacements in itertools.product('ATCG', repeat=d):
            mutation = list(kmer)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            result.append("".join(mutation))
    return list(set(result))  # get rid of duplicates


# All possible kmer patterns in the DNA with at most d mutations
patterns = []
for index in range(len(text) - k + 1):
    kmer = text[index:index+k]
    patterns += mutations(kmer, d)
patterns = list(set(patterns))


for pattern in patterns:
    rc_pattern = ""
    for i in range(len(pattern)):
        rc_pattern += dna_mapping[pattern[-i - 1]]

    for i in range(len(text) - k + 1):
        mismatch, rc_mismatch = 0, 0

        for j in range(k):
            if pattern[j] != text[i + j]:
                mismatch += 1
                if mismatch > d:
                    break

        for j in range(k):
            if rc_pattern[j] != text[i + j]:
                rc_mismatch += 1
                if rc_mismatch > d:
                    break

        if mismatch <= d:
            if pattern in freq:
                freq[pattern] += 1
            else:
                freq[pattern] = 1

        if rc_mismatch <= d:
            if pattern in freq:
                freq[pattern] += 1
            else:
                freq[pattern] = 1


max_freq = max(freq.values())

for k in freq.keys():
    if freq[k] == max_freq:
        print k,

