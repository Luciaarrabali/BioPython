# Autor: Carmen Lucía Arrabalí Cañete

import DNA
import ReverseCom

def hamming1(lhs, rhs):
    total = 0
    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            total += 1
    return total
print(hamming1(DNA.dna, ReverseCom.reverse_complement(DNA.dna)))

list(enumerate('ACGT'))
def hamming2(lhs, rhs):
    set1 = set([(x,y) for x,y in enumerate(lhs)])
    set2 = set([(x,y) for x,y in enumerate(rhs)])
    return len(set1.difference(set2))
print(hamming2(DNA.dna, ReverseCom.reverse_complement(DNA.dna)))


list(zip('ACTG','GTCA'))
def hamming3(lhs, rhs):
    return len([(x,y) for x,y in zip(lhs, rhs) if x != y])
print(hamming3(DNA.dna, ReverseCom.reverse_complement(DNA.dna)))