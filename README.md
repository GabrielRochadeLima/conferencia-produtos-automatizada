# 📦 Sistema de Conferência de Produtos

Sistema desenvolvido em **Python** com o objetivo de auxiliar no processo de conferência e bipagem de produtos da logística.

A aplicação permite realizar a leitura dos **EANs dos produtos**, identificar produtos repetidos e somar automaticamente suas quantidades, gerando uma conferência organizada que futuramente poderá ser utilizada para movimentações de estoque.

## 🎯 Objetivo

O projeto surgiu a partir da necessidade de **automatizar e simplificar o processo de conferência de produtos**, reduzindo a necessidade de controles manuais e facilitando a preparação das informações para o aplicativo de movimentação utilizado pela empresa.

A ideia é que o operador possa realizar a conferência utilizando principalmente o leitor de código de barras, enquanto o sistema fica responsável por organizar os dados.

## 🚀 Funcionalidades atuais

* Iniciar uma nova conferência.
* Gerar automaticamente um número para cada conferência.
* Realizar a bipagem dos produtos através do EAN.
* Identificar EANs repetidos.
* Somar automaticamente a quantidade de cada produto.
* Finalizar a conferência através do comando `fim`.
* Exibir um resumo dos produtos conferidos.
* Manter a sequência do número das conferências através de arquivo `.txt`.

## 🖥️ Exemplo de utilização

Ao iniciar o programa:

```text
=== BEM-VINDO AO SISTEMA DE CONFERÊNCIA ===

1 - Iniciar conferência

Digite a opção: 1

=== CONFERÊNCIA 0001 ===

Bipe o EAN: 789123
Produto adicionado com sucesso!

Bipe o EAN: 789123
Produto adicionado com sucesso!

Bipe o EAN: 789456
Produto adicionado com sucesso!

Bipe o EAN: fim
Lista de produtos finalizada com sucesso!
```

Ao finalizar:

```text
=== CONFERÊNCIA FINALIZADA ===

Conferência: 0001

Produtos:

EAN: 789123 | Quantidade: 2
EAN: 789456 | Quantidade: 1
```

## 🧠 Como funciona

O sistema utiliza um **dicionário Python** para controlar os produtos bipados.

Exemplo:

```python
produtos = {
    "789123": 2,
    "789456": 1
}
```

Quando um EAN é bipado novamente, sua quantidade é incrementada automaticamente.

```python
if ean in produtos:
    produtos[ean] += 1
else:
    produtos[ean] = 1
```

Dessa forma, não é necessário manter uma lista com várias ocorrências do mesmo produto.

## 🔢 Numeração das conferências

O sistema utiliza o arquivo:

```text
numero_conferencia.txt
```

para controlar a sequência das conferências.

Exemplo:

```text
0001
0002
0003
0004
```

Isso permite que novas conferências continuem a numeração mesmo depois que o programa for encerrado.

## 🛠️ Tecnologias utilizadas

* **Python**
* Estruturas de dados `dict`
* Manipulação de arquivos `.txt`
* Entrada de dados pelo terminal

## 📁 Estrutura atual do projeto

```text
sistema-conferencia/
│
├── conferencia.py
├── numero_conferencia.txt
└── README.md
```

> O arquivo `numero_conferencia.txt` é utilizado pelo sistema para controlar a numeração das conferências.

## 🔮 Próximos passos

O projeto ainda está em desenvolvimento. Entre as próximas funcionalidades planejadas estão:

* [ ] Salvar cada conferência realizada.
* [ ] Permitir consultar conferências anteriores pelo número.
* [ ] Associar **EAN → SKU**.
* [ ] Exibir SKU, EAN e quantidade na conferência.
* [ ] Gerar uma lista em formato adequado para movimentação.
* [ ] Exportar os dados para Excel/CSV.
* [ ] Integrar com o aplicativo de movimentação da empresa.
* [ ] Utilizar banco de dados para armazenar as conferências.
* [ ] Melhorar a interface e experiência de utilização.
* [ ] Validar EANs antes de adicioná-los à conferência.

## 📌 Visão futura

A ideia é evoluir o projeto para que o processo seja:

```text
Bipagem
   ↓
Identificação do EAN
   ↓
Agrupamento dos produtos
   ↓
Soma das quantidades
   ↓
EAN → SKU
   ↓
Geração da lista
   ↓
Movimentação de estoque
```

O objetivo final é reduzir etapas manuais no processo logístico e tornar a conferência mais rápida, organizada e confiável.

## 👨‍💻 Desenvolvimento

Projeto desenvolvido como iniciativa de **automação de processos logísticos**, utilizando Python para transformar um processo operacional em uma solução automatizada.

**Status:** 🚧 Em desenvolvimento

