# Cyclopeptide sequencing branch and bound algorithm

import sys
from operator import eq
import itertools as it

lines = open(sys.argv[1].strip(), 'r').readlines()
spectrum = map(int, str(lines[0]).strip().split(" "))

mass = [57, 71, 87, 97, 99, 101, 103, 113, 114,
        115, 128, 129, 131, 137, 147, 156, 163, 186]


def cut_peptide(peptide):
    result = []
    for cut in range(1, len(peptide)):  # cut size
        for i in range(len(peptide) - cut):
            result.append(peptide[i:i + cut])
            result.append(peptide[i + cut:] + peptide[:i])  # cyclic peptide
    result.append(peptide)
    return result


def expand(l):
    lc = l[:]  # list copy
    for i in lc:
        l.remove(i)
        for m in mass:
            temp = i[:]  # list copy
            temp.append(m)
            l.append(temp)


def is_consistent(peptide, spectrum):
    spectrum_copy = spectrum[:]
    for sp in peptide:
        if sp not in spectrum_copy:
            return False
        else:
            spectrum_copy.remove(sp)
    return True


def compare_list(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                pass
            else:
                return False
        return True
    else:
        return False


def cyclopeptide_sequencing(spectrum):
    l = [[]]
    while len(l) != 0:
        expand(l)
        for peptide in l:
            # print peptide
            p_spectrum = [0] + [sum(s) for s in cut_peptide(peptide)]
            if sorted(p_spectrum) == spectrum:
                print "-".join([str(x) for x in peptide])
                l.remove(peptide)
            else:
                if not is_consistent(peptide, spectrum):
                    l.remove(peptide)


if __name__ == "__main__":
    cyclopeptide_sequencing(spectrum)
