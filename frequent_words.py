# Frequent Words

import sys


def frequent_words(text, k):
    """
    >>> frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    ['CATG', 'GCAT']
    """

    l = len(text)
    d = {}

    for i in range(l - k + 1):
        kmer = text[i:i + k]
        if kmer in d:
            d[kmer] += 1
        else:
            d[kmer] = 1

    max_frequency = max(d.values())
    return [kmer for kmer, freq in d.items() if freq == max_frequency]


if __name__ == "__main__":
    lines = open(sys.argv[1].strip(), 'r').readlines()
    text = str(lines[0].strip())
    k = int(lines[1].strip())

    print(" ".join(frequent_words(text, k)))
