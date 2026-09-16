import random
numero_computador = random.randint(1, 5)
print('O computador pensou em um numero, tente adivinhar qual foi esse numero!!!')
usuario = input('Digite um numero de 1 a 5: ')

if usuario == numero_computador:
    print('Parabens, você acertou o numero!!')
else:
    print(f'Que pena, você errou!\n'
          f'O numero pensado era: {numero_computador}\n')


