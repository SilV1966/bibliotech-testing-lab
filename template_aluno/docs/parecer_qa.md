# Missão QA — BiblioTech

## Requisitos testados
- [x] RF01
- [x] RF02
- [x] RF03

## Caixa preta
Quantidade de testes: 12 casos principais.

Casos de fronteira utilizados:
- RF01: 0 e 3 empréstimos;
- RF02: 0, 1, 7 e 8 dias;
- RF03: 0, 1, 8 e 31 dias.

## Caixa branca
Foi analisada a estrutura condicional das funções e acrescentado o CT-05 para exercitar o caminho de rejeição quando `emprestimos_ativos` é superior ao limite.

## Defeitos encontrados
No RF01, o requisito determina que o usuário precisa possuir menos de 3 empréstimos ativos. Portanto, com exatamente 3 empréstimos, o resultado esperado é `False`.

O CT-04 apresentou `True`, evidenciando divergência entre o comportamento implementado e o requisito.

## Evidências
**Resultado do pytest:** o CT-04 deve falhar, evidenciando o defeito proposital.

**Resultado de cobertura:** executar:
`pytest --cov=src --cov-branch --cov-report=term-missing`

Registrar aqui o percentual apresentado pelo ambiente da equipe.

## Parecer da equipe
- [ ] Recomendamos aprovação
- [x] Não recomendamos aprovação

### Justificativa
Não recomendamos a liberação da versão enquanto o defeito identificado no RF01 permanecer, pois o comportamento observado viola diretamente uma regra funcional crítica de empréstimo. Os testes automatizados fornecem evidência reproduzível do problema.
