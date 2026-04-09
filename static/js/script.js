const API = "/usuarios";

// CARREGAR USUÁRIOS
function carregarUsuarios() {
    fetch(API)
    .then(res => res.json())
    .then(data => {
        const lista = document.getElementById("lista");
        lista.innerHTML = "";

        data.forEach(u => {
            const div = document.createElement("div");
            div.className = "usuario";

            div.innerHTML = `
                <div class="info">
                    <span><strong>Nome:</strong> ${u.nome}</span>
                    <span><strong>Email:</strong> ${u.email}</span>
                </div>

                <div class="acoes">
                    <button class="edit" onclick="editar('${u.id}', '${u.nome}', '${u.email}')">Editar</button>
                    <button class="excluir" onclick="deletar('${u.id}')">Excluir</button>
                </div>
            `;

            lista.appendChild(div);
        });
    });
}

// CRIAR USUÁRIO
function criarUsuario() {
    console.log("clicou!");

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    if (!nome || !email) {
        alert("Preencha todos os campos!");
        return;
    }

    fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ nome, email })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        limparCampos();
        carregarUsuarios();
    })
    .catch(err => console.error(err));
}

// DELETAR
function deletar(id) {
    fetch(`${API}/${id}`, {
        method: "DELETE"
    }).then(() => carregarUsuarios());
}

// EDITAR
function editar(id, nome, email) {
    const novoNome = prompt("Novo nome:", nome);
    const novoEmail = prompt("Novo email:", email);

    if (!novoNome || !novoEmail) return;

    fetch(`${API}/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            nome: novoNome,
            email: novoEmail
        })
    }).then(() => carregarUsuarios());
}

// LIMPAR
function limparCampos() {
    document.getElementById("nome").value = "";
    document.getElementById("email").value = "";
}

// INICIAR
document.addEventListener("DOMContentLoaded", () => {
    carregarUsuarios();

    document
        .getElementById("btnCriar")
        .addEventListener("click", criarUsuario);
});