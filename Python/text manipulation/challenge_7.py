nome_bruto = input('Digite seu nome: ')
formatado = nome_bruto.strip().title()
name_split = formatado.split()
primeiro_nome = name_split[0].lower()
segundo_nome = name_split[-1].lower()
email = f'{primeiro_nome}.{segundo_nome}@empresa.com'
print(f"Nome original:  '{nome_bruto}'")
print(f"Nome formatado: {formatado}")
print(f"E-mail gerado:  {email}")