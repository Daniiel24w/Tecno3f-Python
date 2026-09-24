
##Ejercicios

# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos
conjuntoA = {1, 2, 3, 4}
conjuntoB = {3, 4, 5, 6}
# Union de A con B 
resultado = conjuntoA | conjuntoB

print("Union (en A o B, o en ambos):", resultado)


# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B
conjuntoA = {1, 2, 3, 4}
conjuntoB = {3, 4, 5, 6}
# Interseccion de A con B
resultado = conjuntoA & conjuntoB

print("Intersección (en A y B):", resultado)


# Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
conjuntoA = {1, 2, 3, 4}
conjuntoB = {3, 4, 5, 6}
# Diferencia entre A y B
resultado = conjuntoA ^ conjuntoB

print("Diferencia simétrica (en A o B, pero no en ambos):", resultado)


# Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
conjuntoA = {1, 2}
conjuntoB = {1, 2, 3, 4}
# Uso del operador <= o A.issubset(B)
es_subconjunto = conjuntoA <= conjuntoB

if es_subconjunto:
    print("El conjunto A SI es un subconjunto de B.")
else:
    print("El conjunto A NO es un subconjunto de B.")

# Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.
conjuntoA = {10, 20, 30, 40, 50}
cantidad = len(conjuntoA)

print("El número de elementos en el conjunto A es:", cantidad)