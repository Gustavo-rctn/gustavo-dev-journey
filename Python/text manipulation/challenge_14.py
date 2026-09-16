dados_vendas = " CAMISETA:50.0:2 ; CALCA:120.0:1 ; CAMISETA:50.0:tres ; CORROMPIDO ; camiseta:50.0:4 "

quantidade_total_sp = 0
preco = 0.0
faturamento_camisetas = 0.0
pacotes_descartados = 0
vendas_camisetas_validas = 0

lista_pacotes = dados_vendas.split(';')

for pacotes in lista_pacotes:
    pacote_limpo = pacotes.strip()

    partes = pacote_limpo.split(':')

    if len(partes) != 3:
        pacotes_descartados += 1
        continue

    nome = partes[0].strip().upper()
    preco = partes[1].strip()
    quantidade = partes[2].strip()

    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        pacotes_descartados += 1
        continue

    if nome == 'CAMISETA':
        dinheiro = preco * quantidade
        faturamento_camisetas += dinheiro
        vendas_camisetas_validas += 1
        print(f"-> Pacote {nome} processado com sucesso!")

# 5. Relatório Final
print("\n=== RELATÓRIO DE VENDAS (LOJA) ===")
print(f"Vendas válidas de Camiseta: {vendas_camisetas_validas}")
print(f"Faturamento Total com Camisetas: R${faturamento_camisetas:.2f}")
print(f"Registros descartados/erros: {pacotes_descartados}")