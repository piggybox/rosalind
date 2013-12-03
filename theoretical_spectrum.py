import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
peptide = str(lines[0]).strip()

mass = {'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186
        }


def cut_peptide(peptide):
    result = []
    for cut in range(1, len(peptide)):  # cut size
        for i in range(len(peptide) - cut):
            result.append(peptide[i:i + cut])
            result.append(peptide[i + cut:] + peptide[:i])  # cyclic peptide
    result.append(peptide)
    return result


def calculate_mass(subpeptide):
    total = 0
    for s in subpeptide:
        total += mass[s]
    return total


result = ['0'] + [str(calculate_mass(s)) for s in cut_peptide(peptide)]
print " ".join(result)
