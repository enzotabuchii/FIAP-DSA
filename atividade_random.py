import random

numeros = [random.randint(1, 1000) for _ in range(200)]

def bubble_sort(lista):
    n = len(lista)
    trocas = 0

    for i in range(n):
        for j in range(n - 1 - i):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, trocas

def selection_sort(lista):
    n = len(lista)
    trocas = 0

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    return lista, trocas

def insertion_sort(lista):
    trocas = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
            trocas += 1

        lista[j + 1] = atual

    return lista, trocas

print(bubble_sort(numeros.copy()))
print(selection_sort(numeros.copy()))
print(insertion_sort(numeros.copy()))
