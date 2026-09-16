def withdraw_money(atm_inventory, client_balance, requested_amount):
    if requested_amount in atm_inventory:
        if client_balance >= requested_amount:
            atm_inventory.remove(requested_amount)
            return client_balance - requested_amount
        else:
            return 'INSUFFICIENT_FUNDS'
    else:
        return 'BILL_UNAVAILABLE'

atm = [100, 100, 50, 50, 20]
balance = 150.0
request = int(input('Enter the bill value you want to withdraw: '))

update = withdraw_money(atm, balance, request)

formatted_money = ', '.join(f'{money}' for money in atm)

if update == 'INSUFFICIENT_FUNDS':
    print('Insufficient funds!')
elif update == 'BILL_UNAVAILABLE':
    print('Bill unavailable in the ATM!')
else:
    print('Withdrawal successful!')
    print(f'Your new balance is: ${update:.0f}')

print(f'Remaining bills in the ATM: {formatted_money}')
