# Gabarito Privado — Missão QA BiblioTech

## Defeito planejado

O requisito RF01 determina:

"O usuário deve possuir menos de 3 empréstimos ativos."

Portanto:

0 → permitido
1 → permitido
2 → permitido
3 → recusado
4 → recusado

A implementação contém:

```python
if emprestimos_ativos > LIMITE_EMPRESTIMOS:
    return False
