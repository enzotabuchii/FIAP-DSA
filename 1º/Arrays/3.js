// Encontre o maior valor do vetor sem usar funções prontas.

let dados = [8, 15, 3, 27, 12]
let maior = dados[0]

for (i in dados)
    if (dados[i] > maior)
        maior = dados[i]

console.log(maior)