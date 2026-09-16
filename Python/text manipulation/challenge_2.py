number = input("Enter a number (0 to 9999): ")
number_stripe = number.strip()
number_unidade = number_stripe[3]
number_dezena = number_stripe[2]
number_centena = number_stripe[1]
number_milhar = number_stripe[0]
print(f'Unidade: {number_unidade}')
print(f'Dezena: {number_dezena}')
print(f'Centena: {number_centena}')
print(f'Milhar: {number_milhar}')