# 1. Dado bruto que chega no sistema
dados_pacotes = " PAC-01:SP:12.5 ; pac-02:RJ:5.0 ; PAC-03:SP:dois ; INVALIDO ; PAC-04:SP:8.0 "

# 2. Variáveis para acumular o resultado
peso_total_sp = 0.0
pacotes_descartados = 0
pacotes_sp_validos = 0

# 3. Pica a string inteira no ponto e vírgula ";"
lista_pacotes = dados_pacotes.split(';')

# 4. Passa de pacote em pacote
for pacote in lista_pacotes:
    # Limpa os espaços das pontas
    pacote_limpo = pacote.strip()

    # Pica nos dois-pontos ":"
    partes = pacote_limpo.split(':')

    # VALIDAÇÃO 1: Se não tiver exatamente 3 partes (Código, Cidade, Peso), descarta
    if len(partes) != 3:
        pacotes_descartados += 1
        continue  # Pula pro próximo pacote da lista

    # Extrai os dados das posições
    codigo = partes[0].strip().upper()
    cidade = partes[1].strip().upper()
    peso_texto = partes[2].strip()

    # VALIDAÇÃO 2: Tenta converter o peso pra float usando try/except
    try:
        peso = float(peso_texto)
    except ValueError:
        # Se veio texto no peso (ex: "dois"), o float() falha e cai aqui
        pacotes_descartados += 1
        continue  # Pula pro próximo pacote da lista

    # REGRA DE NEGÓCIO: Se o pacote for pra SP, soma o peso
    if cidade == "SP":
        peso_total_sp += peso
        pacotes_sp_validos += 1
        print(f"-> Pacote {codigo} processado com sucesso! Peso: {peso}kg")

# 5. Relatório Final
print("\n=== RELATÓRIO DE ENTREGAS (SP) ===")
print(f"Pacotes válidos enviados pra SP: {pacotes_sp_validos}")
print(f"Peso total acumulado pra SP: {peso_total_sp} kg")
print(f"Pacotes corrompidos/descartados: {pacotes_descartados}")