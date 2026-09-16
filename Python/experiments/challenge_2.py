def add_product(cart, item):
    cart.append(item)
    return cart

my_cart = ['candy', 'rice', 'water']

new_product = input('Enter the product to add: ').strip().lower()
update_cart = add_product(my_cart, new_product)

print(f'Shopping list: {my_cart}\n'
      f'Item added: {new_product}\n'
      f'Updated list: {update_cart}\n')
