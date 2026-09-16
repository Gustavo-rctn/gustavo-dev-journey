def analisar_emprestimo(renda, score, valor_emprestimo, numero_parcelas):
    # 1. PASSO DE PREPARAÇÃO (Cálculos necessários)
    valor_parcela = valor_emprestimo / numero_parcelas
    limite_parcela = renda * 0.30

    # 2. PASSO DE VALIDAÇÃO (Barreiras / Guard Clauses)
    if renda < 2000:
        return 'REPROVADO_RENDA'

    elif score < 600:
        return 'REPROVADO_SCORE'

    elif valor_parcela > limite_parcela:
        return 'REPROVADO_PARCELA_ALTA'

    # 3. PASSO DE SUCESSO (Caminho Feliz)
    else:
        return 'APROVADO'


renda_digitada = float(input('Digite a renda digitada: '))
score_digitado = float(input('Digite o seu score: '))
valor_emprestimo_digitado = float(input('Digite o valor do emprestimo: '))
parcelas_digitadas = int(input('Digite a quantidade de parcelas: '))

# Chamada da função passando os dados digitados
update_emprestimo = analisar_emprestimo(renda_digitada, score_digitado, valor_emprestimo_digitado, parcelas_digitadas)

# --- Suas mensagens no final ---
if update_emprestimo == 'REPROVADO_RENDA':
    print('Sua renda é menor que R$2000, não é possivel fazer o emprestimo!')
elif update_emprestimo == 'REPROVADO_SCORE':
    print('Seu SCORE é baixo demais!')
elif update_emprestimo == 'REPROVADO_PARCELA_ALTA':
    print('O valor das parcelas compromete mais de 30% da sua renda!')
else:
    print('Emprestimo APROVADO!')
