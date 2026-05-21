// "lista encadeada" simulada
let valores = [];
let proximo = [];

let inicio = -1;
let ultimo = -1;

function adicionar() {
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
    document.getElementById("saida").innerHTML = "Elemento adicionado!";
}

function mostrar() {
    alert(valores);
}
