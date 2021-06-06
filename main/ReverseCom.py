# Autor: Carmen Lucía Arrabalí Cañete

from main import DNA

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A',
                  'C': 'G', 'G': 'C'}
    rc = ''
    for base in dna:
        rc += complement[base]
    return ''.join(reversed(rc))

print(DNA.dna, reverse_complement(DNA.dna))