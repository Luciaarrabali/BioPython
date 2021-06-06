# Autor: Carmen Lucía Arrabalí Cañete

from main import DNA
from collections import Counter
from typing import List, Tuple

def motifs(dna: str, k: int, n: int = 5) -> List[Tuple[str, int]]:
    motifs = Counter([dna[i:i+k] for i in range(len(dna)-k+1)])
    return motifs.most_common(n)