def calcular_frete(valor_compra, e_prime, regiao_distante_km):
    # 1. Define o frete base inicial
    frete = 20.0

    # 2. Aplica a regra de Frete Grátis (zerando o frete base)
    if valor_compra >= 200 or e_prime == True:
        frete = 0.0

    # 3. Aplica a taxa de distância se for acima de 300km (soma R$ 15 ao frete atual)
    if regiao_distante_km > 300:
        frete = frete + 15.0

    # 4. Devolve o valor final calculado
    return frete


# --- ENTRADA DE DADOS ---
compra = float(input('Digite o valor da compra (R$): '))
resposta_prime = input('É membro Prime? (S/N): ').upper()
distancia = float(input('Digite a distância da entrega em KM: '))


# Converte a resposta do Prime para True ou False (Booleano)
cliente_prime = resposta_prime == 'S'

# --- CHAMADA DA FUNÇÃO ---
valor_final_frete = calcular_frete(compra, cliente_prime, distancia)

# --- RESULTADO ---
print(f'O valor do frete para essa compra é: R$ {valor_final_frete:.2f}')