import re

def validar_cpf(cpf):
    # Remove caracteres não numerais da entrada
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)

    # Verifica se o CPF possui 11 dígitos
    if len(cpf_limpo) != 11:
        print('CPF inválido. Certifique-se de inserir 11 dígitos.')
        return False

    # Verifica se todos os dígitos são iguais
    if cpf_limpo == cpf_limpo[0] * len(cpf_limpo):
        print('CPF inválido. Todos os dígitos são iguais.')
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 10
    for digito in cpf_limpo[:9]:
        soma += int(digito) * peso
        peso -= 1

    resto_divisao = soma % 11
    digito_verificador_1 = 0 if resto_divisao < 2 else 11 - resto_divisao

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 11
    for digito in cpf_limpo[:10]:
        soma += int(digito) * peso
        peso -= 1

    resto_divisao = soma % 11
    digito_verificador_2 = 0 if resto_divisao < 2 else 11 - resto_divisao

    # Verifica se os dígitos calculados correspondem aos dígitos reais do CPF
    if int(cpf_limpo[9]) == digito_verificador_1 and int(cpf_limpo[10]) == digito_verificador_2:
        return True
    else:
        return False

# Entrada do usuário
entrada = input('Digite o CPF que deseja consultar: ')
cpf_limpo = re.sub(r'[^0-9]', '', entrada)

# Chama a função e exibe o resultado
if validar_cpf(entrada):
    # Formata o CPF para exibição
    print(f'{cpf_limpo} é um CPF válido.')
else:
    print(f'{cpf_limpo} é um CPF inválido.')
