# == Q1 ==
# Função 1 
n = 24
def reduzir(n):
    print(n)
    if n <= 1:
        return
    reduzir(n // 2)
reduzir(n)

# Função 2
n = 24
def reduzir2(n):
    if n <= 1:
        return
    reduzir2(n // 2)
    reduzir2(n // 2)
reduzir2(n)


# == Q2 ==
V = [9, 2, 7, 1, 8, 3, 6, 4]
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge(esquerda, direita)
merge_sort(V)


# == Q3 ==
V = [9, 2, 7, 1, 8, 3, 6, 4]

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# == Q4 == e == Q5 ==

# Q4
esquerda = [3, 8]
direita = [5, 7]

# Q5
esquerda = [8, 3]
direita = [5, 7]

def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

print(merge(esquerda, direita))

# == Q6 ==
V = [9, 2, 7, 1, 8, 3, 6, 4]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    menores = []
    iguais = []
    maiores = []
    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)
    resultado_ordenado = quick_sort(menores) + iguais + quick_sort(maiores)
    return resultado_ordenado
quick_sort(V)

# == Q8 ==