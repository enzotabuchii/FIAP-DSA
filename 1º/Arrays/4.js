// Retorne a posição de um valor no vetor. Se não existir, exiba -1.
let dados = [10, 20, 30, 40, 50]
let procurado = 30
let posicao = -1

for (i in dados)
    if (dados[i] === procurado)
        posicao = i

console.log(posicao);
