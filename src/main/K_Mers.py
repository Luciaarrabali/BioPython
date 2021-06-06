# Autor: Carmen Lucía Arrabalí Cañete

from typing import List


def k_mer(dna: str, k: int) -> List[str]:
    return [dna[i:i+k] for i in range(len(dna)-k+1)]