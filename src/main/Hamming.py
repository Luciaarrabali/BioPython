# Autor: Carmen Lucía Arrabalí Cañete

from src.main import DNA
from src.main.ReverseCom import reverse_complement

list(zip('ACTG','GTCA'))

def hamming(lhs, rhs):
    return len([(x,y) for x,y in zip(lhs, rhs) if x != y])

print(hamming(DNA.dna, reverse_complement(DNA.dna)))