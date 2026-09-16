dados_sensores = " SENS-01:ATIVO:42.5 ; SENS-02:INATIVO:20.0 ; SENS-03:ATIVO:quente ; ERRO_LEITURA ; SENS-04:ativo:37.5 "

soma_temperatura = 0.0
sensores_ativos_validos = 0
leituras_descartadas = 0

lista_sensores = dados_sensores.split(';')


for sensores in lista_sensores:
    partes_relatorio = sensores.split(':')



    if len(partes_relatorio) !=3 :
        leituras_descartadas += 1
        continue

    id_sensor = partes_relatorio[0].strip()
    status = partes_relatorio[1].strip().upper()
    temperatura = partes_relatorio[2].strip()

    try:
        temperatura = float(temperatura)
    except ValueError:
        leituras_descartadas += 1
        continue

    if status == 'ATIVO':
        soma_temperatura += temperatura
        sensores_ativos_validos += 1

if sensores_ativos_validos > 0:
    media = soma_temperatura / sensores_ativos_validos
else:
    media = 0.0

print('======== RELATORIO ========')
print(f'Sensores ativos validos: {sensores_ativos_validos}')
print(f'Soma de temperatura: {soma_temperatura}')
print(f'Leituras escartadas: {leituras_descartadas}')
print(f'Média de temperatura: {media}')








