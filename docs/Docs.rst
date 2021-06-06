BioPython
===========
Tarea 8: Vídeo sobre Bioinformática y Python. Proyecto Python y pruebas correspondientes.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Se trata de un repositorio dedicado a un proyecto software en Bioinformática utilizando Python con un curso de Programación Avanzada en Bioinformática.

El vídeo en el que se basa este repositorio "Bioinformática con Python" fue desarrollado para mostrar el potencial de python para resolver problemas en bioinformática con muy pocas líneas de código. Contiene 7 módulos con las funciones más básicas utilizadas en este ámbito, la bioinformática.

DNA
^^^^^^^^
Esta aplicación trata sobre la generación de secuencias de DNA de forma aleatoria. En un lenguaje como Python es bastante sencillo puesto que con el uso de la función ``choice()`` del paquete random se crea una lista y se convierte en una cadena de carácteres con la función ``join()``:

>>> random_DNA(10)
'ACGACGTACG'

GC_Content
^^^^^^^^^^^^^^^^
La siguiente aplicación versa sobre el cálculo del porcentaje de diferentes nucleótidos en una secuencia concreta. En este caso se calcula el porcentaje que hay de nucleóticos 'G' y 'C', los cuales serán extraídos de la aplicación anterior para no basar el ejercicio en un ejemplo concreto ya que esos datos son aleatorios. Como hay varias formas de calcular ese porcentaje, se van a ir diferenciando por versiones, puesto que el mismo código puede comprimirse de varias formas.

Se utiliza la función ``count()``, la cual cuenta las veces que aparece el parámetro que se le pone como "condición". En ente caso, esa condición es la subsecuencia que se está buscando.:

>>> seq = 'ACGT'
>>> gc_content(seq)
0.5


Reverse Complement
^^^^^^^^^^^^^^^^^^^^^^^^
Calcula la reversa complementaria de una cadena de DNA.:

>>> seq = 'GTCATCCG'
>>> revese_complement()
'CGGATGAC'


Hamming distance
^^^^^^^^^^^^^^^^^^^^^^^^
Se basa en contar en cuantos lugares hay dos carácteres distintos. En la primera versión se inicia un contador donde se irán añadiendo el número de veces que dos bases nitrogenadas no coinciden, por lo que será necesario recorrer la secuencia y contar cada una de esas bases.:

>>> lhs = 'ACGT'
>>> rhs = 'TCGA'
>>> hamming(lhs, rhs)
2


Cálculo de K-mers
^^^^^^^^^^^^^^^^^^^^^^^^
Un k-mers es una subsecuencia de longitud K contenida dentro de una secuencia biológica, en este caso se usará el ADN.:

>>> seq = 'ACGT'
>>> k_mer(seq, 3)
['ACG','CGT']

Finding motifs
^^^^^^^^^^^^^^^^^
Se trata de patrones cortos y recurrentes en una secuencia de ADN que pueden tener una función biológica concreta. En este ejemplo solo es necesario encontrar el número de apariciones de los distintos k-mers en la secuencia.:

>>> seq = 'ACGACTAC'
>>> k = 2
>>> n_results = 4
>>> motifs(seq, k, n_results)
[('AC', 3), ('CG', 1), ('GA', 1), ('CT', 1)]

Rabbits
^^^^^^^^^^^^^^
Calcula la población de conejos siguiendo la sucesión de Fibonacci.:

>>> fibonacci(20)
10946
