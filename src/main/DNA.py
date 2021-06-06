# Autor: Carmen Lucía Arrabalí Cañete

import random

def random_DNA(length: int) -> str:
    dna = ''.join([random.choice('ACGT') for _ in range(length)])
    return(dna)