dados_rh = " CARLOS:TI:10 ; ANA:FINANCEIRO:5 ; BEATRIZ:TI:oito ; REGISTRO_NULO ; FELIPE:ti:12 "

total_horas_ti = 0.0
funcionarios_ti_validos = 0
erros_rh = 0

lista_dado_rh = dados_rh.split(';')

for ti in lista_dado_rh:
    partes_relatorio = ti.strip().split(':')

    if len(partes_relatorio) !=3:
        erros_rh += 1
        continue

    nome = partes_relatorio[0].upper().strip()
    departamento = partes_relatorio[1].upper().strip()
    horas = partes_relatorio[2].strip()

    try:
        total_horas_ti += int(horas)
    except ValueError:
        erros_rh += 1
        continue

    if departamento == 'TI':
        
        funcionarios_ti_validos += 1


print('======== RELATORIO ========')
print(f'Total de horas acumulada pelo departamento de TI: {total_horas_ti}')
print(f'Quantidade de funionarios válidos: {funcionarios_ti_validos}')
print(f'Erros: {erros_rh}')





