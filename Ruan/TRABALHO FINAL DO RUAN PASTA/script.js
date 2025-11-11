// === Dados iniciais ===
let estoque = {
    arroz: 1000,
    feijao: 1000,
    carne: 500,
    salada: 300,
    batata: 400,
    macarrao: 500,
    peixe: 300,
    "carne de porco": 400,
    "carne de frango": 400
};

const consumo = {
    G: { arroz:100, feijao:50, carne:25, salada:10, batata:20, macarrao:30, peixe:20, "carne de porco":25, "carne de frango":25 },
    P: { arroz:50, feijao:25, carne:15, salada:5, batata:10, macarrao:15, peixe:10, "carne de porco":15, "carne de frango":15 }
};

const precos = { G: 25, P: 15 };
let faturamento = 0;
let vendas = { G: 0, P: 0, bebidas: {} };

// === Funções ===
function abrirMenu(menu) {
    document.querySelectorAll(".menu").forEach(m => m.classList.add("oculto"));
    if (menu === 'vendas') document.getElementById("vendas-menu").classList.remove("oculto");
    if (menu === 'estoque') {
        document.getElementById("estoque-menu").classList.remove("oculto");
        mostrarEstoque();
    }
}

function voltarMenu() {
    document.querySelectorAll(".menu").forEach(m => m.classList.add("oculto"));
    document.getElementById("main-menu").classList.remove("oculto");
}

function mostrarEstoque() {
    let html = "";
    for (const [item, qtd] of Object.entries(estoque)) {
        html += `<p>${item}: <strong>${qtd}g</strong></p>`;
    }
    document.getElementById("estoque").innerHTML = html;
}

function adicionarEstoque() {
    for (const item in estoque) {
        let qtd = prompt(`Adicionar quantidade de ${item} (g):`, "0");
        if (qtd && !isNaN(qtd)) estoque[item] += parseFloat(qtd);
    }
    mostrarEstoque();
}

function zerarEstoque() {
    if (confirm("Tem certeza que deseja zerar o estoque?")) {
        for (const item in estoque) estoque[item] = 0;
        mostrarEstoque();
    }
}

function calcularMarmitas(tipo) {
    const cons = consumo[tipo];
    let qtds = [];
    for (const [item, qtd] of Object.entries(cons)) {
        qtds.push(Math.floor(estoque[item] / qtd));
    }
    return Math.min(...qtds);
}

function venderMarmita(tipo) {
    if (calcularMarmitas(tipo) <= 0) {
        alert("Estoque insuficiente!");
        return;
    }

    const cons = consumo[tipo];
    for (const [item, qtd] of Object.entries(cons)) {
        estoque[item] -= qtd;
    }

    vendas[tipo]++;
    faturamento += precos[tipo];

    alert(` Marmita ${tipo === 'G' ? 'GRANDE' : 'PEQUENA'} vendida!`);
    mostrarStatusVendas();
}

function venderBebida() {
    const bebida = prompt("Digite o nome da bebida vendida:");
    const preco = parseFloat(prompt("Digite o valor da bebida:"));

    if (bebida && preco > 0) {
        vendas.bebidas[bebida] = (vendas.bebidas[bebida] || 0) + 1;
        faturamento += preco;
        mostrarStatusVendas();
    }
}

function mostrarStatusVendas() {
    const div = document.getElementById("status-vendas");
    div.innerHTML = `
        <p> Faturamento: R$ ${faturamento.toFixed(2)}</p>
        <p> Marmitas vendidas: G=${vendas.G} | P=${vendas.P}</p>
        <p> Bebidas: ${Object.entries(vendas.bebidas).map(([b,q]) => `${b}: ${q}`).join(", ")}</p>
    `;
}

function mostrarResumo() {
    alert(`
 Faturamento: R$ ${faturamento.toFixed(2)}
 Marmitas grandes: ${vendas.G}
 Marmitas pequenas: ${vendas.P}
 Bebidas: ${Object.keys(vendas.bebidas).length}
    `);
}

function mostrarRelatorioFinal() {
    let relatorio = `
===== RELATÓRIO FINAL =====
 Faturamento total: R$ ${faturamento.toFixed(2)}
Marmitas grandes: ${vendas.G}
Marmitas pequenas: ${vendas.P}
Bebidas vendidas:
`;
    for (const [nome, qtd] of Object.entries(vendas.bebidas)) {
        relatorio += ` - ${nome}: ${qtd}\n`;
    }
    alert(relatorio);
}
