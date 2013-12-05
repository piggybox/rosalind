 # Implement Median String.
 # Input: An integerk,followed by a collection of strings Dna.
 # Output: A k-mer Pattern that minimizes d(Pattern,Dna) among all k-mersPattern.
 # (Return anyone if there are multiple medium strings.)

import sys
import itertools as it

lines = open(sys.argv[1].strip(), 'r').readlines()
k = int(lines[0].strip())
dnas = map(lambda x: x.rstrip(), lines[1:])


def distance(pattern, dna):
    d_min = 100000
    for i in range(len(dna) - len(pattern) + 1):
        d = 0
        for j in range(len(pattern)):
            if pattern[j] != dna[i+j]:
                d += 1
        if d < d_min:
            d_min = d
    return d_min


def cum_distance(pattern, dna_collection):
    return sum(map(lambda x: distance(pattern, x), dna_collection))


best_pattern = 'A' * k
best_distance = 100000
patterns = map("".join, it.product("ATCG", repeat=k))
for p in patterns:
    if cum_distance(p, dnas) < best_distance:
        best_pattern = p
        best_distance = cum_distance(p, dnas)
print best_pattern, best_distance

