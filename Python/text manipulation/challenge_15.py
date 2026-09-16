log_servidor = " admin:SUCESSO:120 ; user1:ERRO:500 ; user2:sucesso:linha_caiu ; BUG ; admin:SUCESSO:80 "

tempo_total_sucesso = 0
erros_descartados = 0
acessos_sucesso_validos = 0

lista_servidor = log_servidor.split(';')

for log in lista_servidor:
    log_limpo = log.strip()

    partes_log = log_limpo.split(':').strip()

    if len(partes_log) != 3:
        erros_descartados += 1
        continue

    usuario = partes_log[0].strip().upper()
    status = partes_log[1].strip().upper()
    tempo_texto = partes_log[2].strip()

    try:
        tempo_texto = int(tempo_texto)
    except ValueError:
        erros_descartados += 1
        continue

    if status == 'SUCESSO':
        tempo_total_sucesso += tempo_texto
        acessos_sucesso_validos += 1

print('======== RELATORIO ========')
print(f'Tempo acumulado: {tempo_total_sucesso} ms')
print(f'Acessos com Sucesso: {acessos_sucesso_validos}')
print(f'Erros/Registros Descartados: {erros_descartados}')