# Autor: Carmen Lucía Arrabalí Cañete

import DNA
import operator

#Se utiliza el valor 2 porque así será más sencillo de ver puesto que es más corto.
k = 2

## Version 1
kmers1 = {}
for i in range(len(DNA.dna) - k + 1):
    motif = DNA.dna[i:i+k]
    if not motif in kmers1:
        kmers1[motif] = 0
    kmers1[motif] += 1

all1 = sorted(kmers1.items(), key=operator.itemgetter(1))
print(all1[-5:])

## Version 2
from collections import defaultdict

kmers2 = defaultdict(int)
for i in range(len(DNA.dna) - k + 1):
    motif = DNA.dna[i:i+k]
    kmers2[motif] += 1

all2 = sorted(kmers2.items(), key=operator.itemgetter(1))
print(all2[-5:])

## Version 3
from collections import Counter

motifs = Counter([DNA.dna[i:i+k] for i in range(len(DNA.dna)-k+1)])
print(motifs.most_common(5))