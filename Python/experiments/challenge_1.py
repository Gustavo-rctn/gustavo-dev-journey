def add_product(cart, item):
    cart.append(item)
    return cart

my_cart = ['beans', 'rice']

new_item = input('Enter the name of the product to add: ').strip().lower()

update_cart = add_product(my_cart, new_item)
print(f'Item added: {new_item}\n'
      f'Updated shopping cart: {update_cart}\n')
