# Autor: Carmen Lucía Arrabalí Cañete

def fibonacci(n):
    parent = 1
    child = 1
    for i in range(n):
        child, parent = parent, parent + child
    return child

for i in range(20):
    print(fibonacci(i), end=' ')