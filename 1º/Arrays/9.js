// Remova o elemento da posição 1, deslocando os demais para a esquerda.
let dados = [10, 20, 30, 40, 50]
let posicao = 1

for (let i = 0; i < dados.length -1; i++)
    dados[i] = dados[i + 1]

dados.pop()
console.log(dados)