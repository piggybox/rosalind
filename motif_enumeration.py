 # Implement Motif Enumeration
 # Input: Integers k and d, followed by a collection of strings Dna.
 # Output: All (k, d)-motifs in DNA.

import sys
import itertools

lines = open(sys.argv[1].strip(), 'r').readlines()
k, d = map(int, lines[0].split(" "))
dnas = map(lambda x: x.rstrip(), lines[1:])


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


#  check if a kmer appears in a DNA with at most d mutations
def check_appearance(dna, kmer, d):
    k = len(kmer)
    for i in range(len(dna) - k + 1):
        mismatch = 0
        for j in range(k):
            if kmer[j] != dna[i + j]:
                mismatch += 1
                if mismatch > d:
                    break
        if mismatch <= d:
            return True
    return False


result = []
for dna in dnas:
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i + k]
        for kmer_m in mutations(kmer, d):
            flag = True
            for dna in dnas:
                if not check_appearance(dna, kmer_m, d):
                    flag = False
            if flag:
                result.append(kmer_m)

for i in list(set(result)):
    print i,
