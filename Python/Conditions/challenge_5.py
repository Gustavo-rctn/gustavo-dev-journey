print('-='*20)
print('Analisador de Triângulo')
print('-='*20)

r1 = float(input('Digite o primeiro numero: '))
r2 = float(input('Digite o segundo numero: '))
r3 = float(input('Digite o terceiro numero: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem virar um triângulo!!')
else:
    print('Não é possivel formar um triângulo!!')

