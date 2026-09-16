# O sistema deve solicitar os e-mails dos visitantes/colaboradores
# O usuario vai colar ou digitar tudo em uma unica linha separando os e-mails por ;
# (Vou fazer um laço for pra ele escrever ou copiar os e-mails que eu acho que fica melhor e mais dinamico)
# Se o usuario digitar um ; a mais no final o sistema não deve dar erro e nem contar a entrada vazia como e-mail descartado, só ignorar e seguir
# Obrigatorio a função validar_email(email) pra checar o domínio
# Cruzar os e-mails válidos com o banco_funcionarios
# SE for valido e estiver no banco: Libera o acesso e mostra o NOME e o CARGO
# SE for inválido ou não cadastrado: Avisa a recusa e incrementa os detalhes
# Ao terminar todos os e-mails digitados, o programa exibe o total de acessos liberados e de recusas também


def validar_email(email):
    if email.endswith('@EMPRESA.COM'):
        return True
    else:
        return False


banco_funcionarios = {
    "CARLOS@EMPRESA.COM": {"nome": "Carlos Silva", "cargo": "Dev Python", "salario": 7500},
    "ANA@EMPRESA.COM": {"nome": "Ana Souza", "cargo": "Analista de Dados", "salario": 8200},
    "FELIPE@EMPRESA.COM": {"nome": "Felipe Lima", "cargo": "Gerente de TI", "salario": 12000}
}

quantidade = int(input('Digite quantos funcionarios você quer encontrar pelo e-mail corporativo: '))
acessos_permitidos = 0
acessos_descartados = 0
cadastro_feito = 0

for quantos in range(0, quantidade ):

        funcionario = input('Digite o e-mail do funcionario que você deseja encontrar os dados: ')  # Exemplo: ANA@EMPRESA.COM

        email_limpo = funcionario.strip().upper()

        if not validar_email(email_limpo):
            acessos_descartados += 1
            print('Funcionario não existe no sistema')
            continue

        if email_limpo in banco_funcionarios:
            funcionario = banco_funcionarios[email_limpo]
            acessos_permitidos += 1

            print('Funcionario encontrado!')

            quanto_dado = int(input('Quantos dados você quer encontrar: '))


            if quanto_dado == 1:
                dados_1 = input('Digite o dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                print(f'Acesso Liberado -> {dados_1}: {funcionario[dados_1]}')
            elif quanto_dado == 2:
                dados_1 = input('Digite o primeiro dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                dados_2 = input('Digite o segundo dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                print(f"Acesso Liberado -> {dados_1}: {funcionario[dados_1]} | {dados_2}: {funcionario[dados_2]}")
            elif quanto_dado == 3:
                dados_1 = input('Digite o primeiro dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                dados_2 = input('Digite o segundo dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                dados_3 = input('Digite o terceiro dado que você deseja encontrar (ex: nome, cargo): ').lower().strip()
                print(f"Acesso Liberado -> {dados_1}: {funcionario[dados_1]} | {dados_2}: {funcionario[dados_2]} | {dados_3}: {funcionario[dados_3]}")

            else:
                print('No banco de funcionarios não existe mais de 4 dados por funcionario')


        else:
            print('E-mail corporativo porém não cadastrado!')

            ask_cadastro = input('Deseja cadastrar o funcionario (S/N) ? ').upper()

            if ask_cadastro == 'S':
                banco_funcionarios_cadastro = input('Digite o e-mail que você quer cadastrar o funcionario: ').upper()
                banco_funcionarios[banco_funcionarios_cadastro] = {}

                banco_funcionarios[banco_funcionarios_cadastro]['nome'] = input('Digite o nome do funcionario: ').strip()
                banco_funcionarios[banco_funcionarios_cadastro]['cargo'] = input('Digite o cargo do funcionario: ').title().strip()
                banco_funcionarios[banco_funcionarios_cadastro]['salario'] = int(input('Digite o salario do funcionario: '))

                print('==================================================================')

                print('Funcionario cadastrado!')
                print(f'E-mail: ', banco_funcionarios_cadastro)
                print(f'Nome: ', banco_funcionarios[banco_funcionarios_cadastro].get('nome'))
                print(f'Cargo: ', banco_funcionarios[banco_funcionarios_cadastro].get('cargo'))
                print(f'Salario: ', banco_funcionarios[banco_funcionarios_cadastro].get('salario'))
                cadastro_feito += 1
            elif ask_cadastro == 'N':
                print('Volte sempre!')
                continue

print('======== RELATORIO ========')
print(f'Acessos Permitidos: {acessos_permitidos}')
print(f'Acessos Negados: {acessos_descartados}')
print(f'Cadastros Feitos: {cadastro_feito}')




