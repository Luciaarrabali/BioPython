# Autor: Carmen Lucía Arrabalí Cañete

from src.main.DNA import random_DNA


def gc_content(dna):
    return float(dna.count('G') + dna.count('C'))/len(dna)