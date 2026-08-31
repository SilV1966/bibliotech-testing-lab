# Missão QA — BiblioTech
## Repositório privado do professor

Este repositório contém todos os artefatos necessários para aplicação da aula
prática sobre Testes de Caixa Preta e Caixa Branca.

Duração: 90 minutos

Tecnologias:

- Python 3.12
- pytest
- pytest-cov
- GitHub
- GitHub Actions

## IMPORTANTE

A pasta:

`gabarito_privado/`

NUNCA deve ser disponibilizada aos estudantes.

O repositório a ser distribuído para os alunos deve conter SOMENTE o conteúdo
da pasta:

`template_aluno/`

---

# Objetivo pedagógico

A atividade simula um pequeno fluxo profissional de Quality Assurance.

O estudante deverá percorrer:

REQUISITOS
    ↓
PLANO DE TESTES
    ↓
CAIXA PRETA
    ↓
TESTES AUTOMATIZADOS
    ↓
CHECKPOINT
    ↓
CAIXA BRANCA
    ↓
COBERTURA
    ↓
RASTREABILIDADE
    ↓
GITHUB / PULL REQUEST
    ↓
CI
    ↓
PARECER DE QA

Existe um defeito intencional no módulo de empréstimos.

O defeito deve ser encontrado pelos estudantes por meio de um teste de
valor-limite.

Não revele sua localização antes da atividade.

---

# Preparação

Antes da aula:

1. Copiar `template_aluno/` para o repositório de cada equipe.
2. Executar `scripts/validar_template.py`.
3. Confirmar que o smoke test passa.
4. Confirmar que o defeito didático continua presente.
5. Confirmar que nenhum arquivo do gabarito foi publicado.

---

# Regra pedagógica fundamental

Durante a etapa de Caixa Preta, os estudantes NÃO devem consultar:

`src/bibliotech.py`

Depois do checkpoint, o professor libera a análise do código para início da
Caixa Branca.

---

# Regra técnica

Os estudantes podem modificar:

`tests/`
`docs/`

Eles NÃO devem modificar:

`src/`

Caso encontrem um defeito, devem documentá-lo em vez de corrigi-lo.

---

# Resultado esperado

Uma equipe que testa corretamente a fronteira do RF01 deverá identificar
uma divergência funcional.

Consequentemente, a pipeline poderá ficar vermelha.

Isso é esperado.

Não avalie a atividade pela cor da pipeline.

Avalie se o estudante:

- criou testes adequados;
- relacionou testes aos requisitos;
- interpretou corretamente a falha;
- analisou cobertura;
- produziu evidências;
- apresentou um parecer técnico coerente.
