# BioPython
#### Tarea 8: Vídeo sobre Bioinformática y Python. Proyecto Python y pruebas correspondientes.

Se trata de un repositorio dedicado a un proyecto software en Bioinformática utilizando Python con un curso de Programación Avanzada en Bioinformática.

El vídeo en el que se basa este repositorio "Bioinformática con Python" fue desarrollado para mostrar el potencial de python para resolver problemas en bioinformática con muy pocas líneas de código. Contiene 7 módulos con las funciones más básicas utilizadas en este ámbito, la bioinformática.

## `DNA`
Genera secuencias de DNA de forma aleatoria.

```bash
>>> random_DNA(10)
'ACGACGTACG'
```

## `GC_Content`
Calcula el porcentaje de los diferentes nucleótidos, G y C en este caso, en una secuencia concreta.

```bash
>>> seq = 'ACGT'
>>> gc_content(seq)
0.5
```

## `Reverse Complement`
Calcula la reversa complementaria de una cadena de DNA.
```bash
>>> seq = 'GTCATCCG'
>>> revese_complement()
'CGGATGAC'
```

## `Hamming distance`
Se basa en contar en cuantos lugares hay dos carácteres distintos.

```bash
>>> lhs = 'ACGT'
>>> rhs = 'TCGA'
>>> hamming(lhs, rhs)
2
```

## `Cálculo de K-mers`
Un k-mers es una subsecuencia de longitud K contenida dentro de una secuencia biológica, en este caso se usará el ADN.

```bash
>>> seq = 'ACGT'
>>> k_mer(seq, 3)
['ACG','CGT']
```

## `Finding motifs`
Encuentra el número de apariciones de los distintos k-mers de una secuencia de DNA concreta.

```bash
>>> seq = 'ACGACTAC'
>>> k = 2
>>> n_results = 4
>>> motifs(seq, k, n_results) 
[('AC', 3), ('CG', 1), ('GA', 1), ('CT', 1)]
```

## `Rabbits`
Calcula la población de conejos siguiendo la sucesión de Fibonacci.

```bash
>>> fibonacci(20) 
10946
```
