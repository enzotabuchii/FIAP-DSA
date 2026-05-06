// Conte quantas vezes um número aparece no vetor.
let dados = [2, 5, 2, 7, 2, 9]
let alvo = 2
let contador = 0

for (i in dados)
    if (dados[i] === alvo)
        contador++

console.log(contador);