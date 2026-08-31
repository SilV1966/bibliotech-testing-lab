# Parecer QA — Modelo

## Decisão

NÃO APROVAR PARA PRODUÇÃO

## Evidência

Durante os testes relacionados ao RF01 foi identificada uma divergência no
valor-limite de três empréstimos ativos.

Segundo o requisito, um usuário que já possui três empréstimos não pode
realizar outro empréstimo.

Durante a execução, o sistema permitiu a operação.

## Resultado esperado

False

## Resultado observado

True

## Impacto

O comportamento viola diretamente uma regra funcional do módulo de
empréstimos.

## Recomendação

Corrigir a implementação e executar novamente:

- testes funcionais;
- testes de fronteira;
- testes de regressão;
- suíte automatizada completa.

Somente após a execução bem-sucedida dos testes a versão deverá ser
reavaliada para produção.
