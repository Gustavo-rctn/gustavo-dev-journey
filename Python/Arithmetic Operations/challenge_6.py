brl_amount = int(input('How many reais do you have in your wallet??'))
usd_rate = 5.19
usd_amount = brl_amount / usd_rate
print(f'You can buy ${usd_amount:.2f} dollars.')