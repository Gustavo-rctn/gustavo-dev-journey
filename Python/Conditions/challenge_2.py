velocidade = int(input("Digite qual foi a velocidade do carro: "))
limite_permitido = 79
multa = 7.00 * (velocidade - limite_permitido)
if velocidade >= 80:
    print(f'Você foi multado em ${multa}')
else:
    print('Boa viagem!!!')