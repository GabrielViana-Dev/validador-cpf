# Validador-cpf
Este projeto oferece uma solução simples em Python para validar Cadastros de Pessoas Físicas (CPFs). O script implementa a lógica de validação conforme descrita no site: Macoratti - Algoritmo de Validação de CPF.

- Link: https://www.macoratti.net/alg_cpf.htm

## Funcionalidades:
- Remoção de caracteres não numéricos e verificação se o CPF possui 11 dígitos.
- Garantia de que todos os dígitos não sejam idênticos.
- Cálculo e verificação dos dígitos verificadores do CPF.

## Uso Básico:
 - Função validar_cpf(cpf)
   
### Parâmetros:
- cpf (str): O CPF a ser validado.
### Retorno:
- True se o CPF for válido.
- False se o CPF for inválido.
