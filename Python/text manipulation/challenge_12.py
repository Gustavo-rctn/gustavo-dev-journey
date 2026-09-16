def validar_email_corporativo(email):
    if email.endswith('@techcorp.com') or email.endswith('@techcorp.com.br'):
        return 'ACESSO PERMITIDO'
    else:
        return 'ACESSO NEGADO'

quantidade = int(input('Digite a quantidade de funcionarios que você quer cadastrar: '))
for c in range(1, quantidade + 1):
    email_ask = input('Digite o email desses funcionarios: ').strip().lower()

    valor = validar_email_corporativo(email_ask)

    print(f'Resultado para a requisição {c}: {valor}\n')

