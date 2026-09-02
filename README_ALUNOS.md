# BiblioTech — Missão QA

Projeto desenvolvido como atividade prática de Qualidade de Software, com foco na aplicação de técnicas de teste de software sobre a biblioteca BiblioTech.

## 👥 Integrantes da equipe

### Integrantes:

Cauã Monteiro de Oliveira | Ana Carolina Macedo Ramos | Anna Carolina Souza Almeida

## 🎯 Objetivo

Realizar a análise e os testes da biblioteca BiblioTech, aplicando técnicas de teste de caixa preta e caixa branca, testes de fronteira, testes automatizados e análise de cobertura.

## 🧪 Atividades realizadas

- Elaboração do Mini Plano de Testes;
- Criação dos roteiros e casos de teste;
- Construção da matriz de rastreabilidade;
- Implementação de testes automatizados utilizando `pytest`;
- Análise de cobertura de linhas e branches;
- Identificação e documentação de defeitos;
- Elaboração do parecer final de QA.

## 📊 Resultado dos testes

Foram executados **14 testes automatizados**:

- ✅ 13 testes aprovados;
- ❌ 1 teste reprovado;
- 📈 Cobertura de linhas: **100%**;
- 📈 Cobertura de branches: **100%**.

O teste reprovado identificou um defeito no RF01 relacionado ao limite de empréstimos ativos.

## 📁 Estrutura da entrega

```text
.
├── docs/
│   ├── plano_testes.md
│   ├── roteiro_testes.md
│   ├── matriz_rastreabilidade.md
│   └── parecer_qa.md
│
├── src/
│   └── bibliotech.py
│
├── tests/
│   ├── test_bibliotech.py
│   └── test_smoke.py
│
└── .github/
    └── workflows/
        └── tests.yml
