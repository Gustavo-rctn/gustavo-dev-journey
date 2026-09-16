telefone = '(19) 99999-9999'
format = telefone.strip().replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
ddd = format[0:2]
numero = format[2:10]
print(f'DDD: {ddd} | Numero: {numero}')
