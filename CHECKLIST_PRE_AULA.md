# Checklist Pré-Aula — 5 minutos

## 1. Verificar Python

Executar:

python --version

Esperado:

Python 3.12.x

---

## 2. Instalar/verificar dependências

Dentro de `template_aluno/`:

python -m pip install -r requirements-dev.txt

Executar:

python -m pytest --version

---

## 3. Smoke test

Executar:

python -m pytest -q

Esperado:

1 passed

Se o smoke test falhar, corrigir o ambiente antes da aula.

---

## 4. Verificar o defeito didático

Executar:

python -c "from src.bibliotech import pode_emprestar; print(pode_emprestar(True, False, 2))"

Esperado:

True

Executar:

python -c "from src.bibliotech import pode_emprestar; print(pode_emprestar(True, False, 3))"

Esperado:

True

O segundo resultado confirma que o defeito didático continua presente.

NÃO CORRIGIR.

---

## 5. Executar o script de validação

Na raiz do repositório do professor:

python scripts/validar_template.py

Esperado:

VALIDAÇÃO CONCLUÍDA COM SUCESSO

---

## 6. Conferência de segurança

Confirmar que o repositório dos estudantes NÃO contém:

- gabarito_privado/
- bibliotech_corrigido.py
- test_bibliotech_gabarito.py
- GABARITO.md
- comentários indicando o defeito.

---

## 7. Conferência GitHub

[ ] Repositório de cada equipe disponível.

[ ] Estudantes possuem acesso.

[ ] GitHub Actions habilitado.

[ ] Branch main existente.

[ ] Pull Requests permitidos.

---

## GO / NO-GO

Somente iniciar a atividade quando:

[ ] smoke test passa;

[ ] defeito didático está presente;

[ ] gabarito está privado;

[ ] GitHub funciona;

[ ] estudantes conseguem acessar o repositório.
