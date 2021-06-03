# Autor: Carmen Lucía Arrabalí Cañete

import DNA

def gc_content(dna):
    return float(dna.count('G') + dna.count('C'))/len(dna)
print(gc_content(DNA.dna))