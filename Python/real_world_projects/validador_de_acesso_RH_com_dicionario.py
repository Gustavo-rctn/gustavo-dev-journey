def validar_email(email):
    # AJUSTE 1: Mudar para maiúsculo para bater com o .upper() do loop
    if email.endswith('@EMPRESA.COM'):
        return True
    else:
        return False

banco_funcionarios = {
    "CARLOS@EMPRESA.COM": {"nome": "Carlos Silva", "cargo": "Dev Python", "salario": 7500},
    "ANA@EMPRESA.COM": {"nome": "Ana Souza", "cargo": "Analista de Dados", "salario": 8200},
    "FELIPE@EMPRESA.COM": {"nome": "Felipe Lima", "cargo": "Gerente de TI", "salario": 12000}
}
lista_emails = " carlos@empresa.com ; ana@gmail.com ; BEATRIZ ; felipe@empresa.com ; REGISTRO_NULO ".upper()

acessos_permitidos = 0
emails_descartados = 0

lista_dos_emails = lista_emails.split(';')

for email in lista_dos_emails:
    email_limpo = email.strip().upper()

    if not validar_email(email_limpo):
        emails_descartados += 1
        continue

    if email_limpo in banco_funcionarios:
        funcionario = banco_funcionarios[email_limpo]
        acessos_permitidos += 1
        # AJUSTE 2: Acessar a variável funcionario diretamente
        print(f"Acesso Liberado -> Nome: {funcionario['nome']} | Cargo: {funcionario['cargo']}")
    else:
        print('E-mail corporativo porém não cadastrado!')
        emails_descartados += 1

print("\n======== RELATORIO ========")
print(f"Acessos permitidos: {acessos_permitidos}")
print(f"E-mails descartados: {emails_descartados}")