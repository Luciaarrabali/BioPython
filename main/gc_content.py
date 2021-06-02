# Autor: Carmen Lucía Arrabalí Cañete

import DNA

def gc_content1(dna):
    gc = 0
    for base in dna:
        if base == 'C' or base == 'G':
            gc += 1
    return float(gc) / len(dna)

print(gc_content1(DNA.dna))

def gc_content2(dna):
    gc = [base for base in dna if base in 'GC']
    return float(len(gc))/len(dna)

print(gc_content2(DNA.dna))

def gc_content3(dna):
    return float(dna.count('G') + dna.count('C'))/len(dna)

print(gc_content3(DNA.dna))