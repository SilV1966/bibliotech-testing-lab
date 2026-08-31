# Roteiro de Aplicação — 90 minutos

## 0–8 minutos — Abertura

Apresente o cenário:

"Vocês fazem parte da equipe de QA do BiblioTech. Uma nova versão está pronta
para produção e vocês precisam apresentar evidências para decidir se ela deve
ser liberada."

Pergunta inicial:

"Como podemos provar que este software funciona?"

Não apresente o código-fonte.

---

## 8–15 minutos — Preparação

Os estudantes:

- clonam o repositório;
- criam a branch;
- ativam o ambiente virtual;
- instalam dependências;
- executam o smoke test.

Resultado esperado:

`1 passed`

---

## 15–23 minutos — Mini Plano de Testes

Os grupos preenchem:

`docs/plano_testes.md`

Orientar:

- escopo;
- estratégia;
- ambiente;
- critérios;
- riscos;
- entregáveis.

Evitar excesso de documentação.

---

## 23–43 minutos — Caixa Preta

Regra:

NÃO ABRIR `src/bibliotech.py`.

Os estudantes devem utilizar apenas:

`requisitos.md`

Exigir pelo menos:

- 4 casos RF01;
- 4 casos RF02;
- 4 casos RF03.

Orientar a turma a pensar em:

- classes de equivalência;
- valores-limite;
- cenários positivos;
- cenários negativos.

Não indique quais valores devem ser testados.

---

## 43–48 minutos — Checkpoint

Interromper a turma.

Perguntar:

1. Qual requisito gerou mais casos?
2. Quais fronteiras foram identificadas?
3. Algum comportamento observado divergiu do requisito?
4. Foi necessário conhecer o código para encontrar a divergência?

Não revele o defeito.

Depois diga:

"Agora vocês estão autorizados a abrir `src/bibliotech.py`."

---

## 48–65 minutos — Caixa Branca

Orientar os grupos a localizar:

- if;
- elif;
- retornos;
- condições;
- caminhos;
- branches.

Perguntas:

"Existe um teste para a condição verdadeira?"

"Existe um teste para a condição falsa?"

"Existe algum caminho ainda não exercitado?"

---

## 65–73 minutos — Cobertura

Executar:

python -m pytest -v --cov=src --cov-branch --cov-report=term-missing

Meta:

90% ou mais.

Pergunta:

"Uma cobertura de 100% prova que os requisitos foram atendidos?"

---

## 73–80 minutos — Rastreabilidade

Preencher:

`docs/matriz_rastreabilidade.md`

Perguntar:

"Existe requisito sem teste?"

"Existe teste sem requisito relacionado?"

---

## 80–86 minutos — GitHub

Executar:

git status
git add tests docs
git commit -m "test: adiciona testes caixa preta e caixa branca"
git push -u origin testes/equipe-XX

Criar Pull Request.

Observar GitHub Actions.

Não exigir pipeline verde.

---

## 86–90 minutos — Parecer de QA

Cada grupo deve decidir:

APROVAR

ou

NÃO APROVAR

A decisão deve utilizar evidências:

- requisitos;
- casos;
- resultados;
- cobertura;
- defeitos;
- CI.

Pergunta final:

"Temos evidências suficientes para confiar nesta versão?"
