# Frequent Words with Mismatches

import sys
import itertools

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()
k, d = map(int, lines[1].split(" "))
freq = {}


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


for index in range(len(text) - k + 1):
    kmer = text[index:index + k]
    for pattern in mutations(kmer, d):
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
