# 'Withdrawal amount' é o termo técnico para o valor que se quer sacar
withdraw_amount = int(input('Enter the withdrawal amount: '))

# Termos em inglês: 'bills' para notas e 'coins' para moedas
bills_50 = withdraw_amount // 50
remainder_50 = withdraw_amount % 50

bills_20 = remainder_50 // 20
remainder_20 = remainder_50 % 20

bills_10 = remainder_20 // 10
remainder_10 = remainder_20 % 10

coins_1 = remainder_10

print(f'\nTransaction Summary:')
print(f'Total Amount: ${withdraw_amount}')
print(f'$50 bills: {bills_50}')
print(f'$20 bills: {bills_20}')
print(f'$10 bills: {bills_10}')
print(f'$1 coins: {coins_1}')
