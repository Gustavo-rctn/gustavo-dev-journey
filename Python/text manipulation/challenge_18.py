dados_banco = " ENTRADA:100.0 ; SAIDA:30.0 ; ENTRADA:cinquenta ; CORROMPIDO ; SAIDA:80.0 "

saldo_total = 0.0
operacoes_validas = 0
erros_descartados = 0

lista_operacoes = dados_banco.split(';')

for tipo_estado in lista_operacoes:
    partes_relatorio = tipo_estado.strip().split(':')

    if len(partes_relatorio) != 2:
        erros_descartados += 1
        continue

    tipo = partes_relatorio[0].upper().strip()
    valor_texto = partes_relatorio[1].strip()

    try:
         valor_num = float(valor_texto)
    except ValueError:
        erros_descartados += 1
        continue

    if tipo == 'ENTRADA':
        saldo_total += valor_num
        operacoes_validas += 1
    elif tipo == 'SAIDA':
        saldo_total -= valor_num
        operacoes_validas += 1

print('======== RELATORIO ========')
print(f'Saldo total: {saldo_total:.2f}')
print(f'Operações válidas: {operacoes_validas}')
print(f'Erros descartados: {erros_descartados}')
