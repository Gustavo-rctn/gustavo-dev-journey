dados_alunos = " CARLOS:8.5 ; ANA:5.0 ; BEATRIZ:dez ; INVALIDO ; FELIPE:7.0 "

total_aprovados = 0
total_reprovados = 0
registros_invalidos = 0

lista_dados = dados_alunos.split(';')

for dados in lista_dados:
    dados_limpos = dados.strip().split(':')

    if len(dados_limpos) != 2:
        registros_invalidos += 1
        continue

    nome = dados_limpos[0].strip().upper
    notas_texto = dados_limpos[1].strip()

    try:
        notas_num = float(notas_texto)
    except ValueError:
        registros_invalidos += 1
        continue

    if notas_num <= 6:
        total_reprovados += 1
    else:
        total_aprovados += 1

print('======== RELATORIO ========')
print(f'Total de alunos reprovados: {total_reprovados}')
print(f'Total de alunos aprovados: {total_aprovados}')
print(f'Total de registros invalidos: {registros_invalidos}')