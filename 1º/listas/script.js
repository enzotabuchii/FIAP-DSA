// "lista encadeada" simulada
let valores = [];
let proximo = [];

let inicio = -1;
let ultimo = -1;

function adicionarFim() {
    let nome = document.getElementById("nome").value;

    if (nome === "") {
        alert("Digite um nome");
        return;
    }

    let novoIndice = valores.length;
    valores.push(nome);
    proximo.push(-1);
    if (inicio === -1) {
        inicio = novoIndice;
        ultimo = novoIndice;
    } else {
        proximo[ultimo] = novoIndice;
        ultimo = novoIndice;
    }

    document.getElementById("nome").value = "";
    mostrar();
}

function adicionarInicio() {
    let nome = document.getElementById("nome").value;

    if (nome === "") {
        alert("Digite um nome");
        return;
    }

    let novoIndice = valores.length;
    
    valores.push(nome);
    proximo.push(inicio);
    inicio = novoIndice;

    if (inicio === -1)
        ultimo = novoIndice;

    document.getElementById("nome").value = "";
    mostrar();
}

function removerInicio() {
    if (inicio === -1) {
        alert("Lista vazia");
        return;
    }

    inicio = proximo[inicio];

    if (inicio === -1)
        ultimo = -1;

    mostrar()
}

function mostrar() {
    let resultado = "";
    let atual = inicio;

    
    while (atual !== -1) {
        resultado += valores[atual] + " => ";
        atual = proximo[atual];
    }

    if (inicio === -1)
        resultado = "Lista vazia";
    else
        resultado += "null";

    document.getElementById("saida").innerHTML = resultado;
}
