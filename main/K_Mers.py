# Autor: Carmen Lucía Arrabalí Cañete

from main import DNA

k = 4
for i in range(len(DNA.dna) - k + 1):
    print(DNA.dna[i:i+k])