price = float(input('what is your price?')) * 0.90
fixed_discount = 0.10 #10%
price_discount = (price * fixed_discount)
final_price = price - price_discount
print(f'the final price is {final_price: .2f}')