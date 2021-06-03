# Autor: Carmen Lucía Arrabalí Cañete

import DNA
from collections import Counter

#Se utiliza el valor 2 porque así será más sencillo de ver puesto que es más corto.
k = 2

motifs = Counter([DNA.dna[i:i+k] for i in range(len(DNA.dna)-k+1)])
print(motifs.most_common(5))