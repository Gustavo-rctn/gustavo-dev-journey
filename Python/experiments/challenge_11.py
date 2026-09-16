def insert_second_item(cart, item):
    cart.insert(1, item)
    return cart

item_list = ['Beans', 'Rice', 'Chocolate']
new_item = input('Enter the item name: ').strip()

updated_cart = insert_second_item(item_list, new_item)
formatted_cart = ', '.join(f'{item}' for item in updated_cart)

print(f'Item list: {formatted_cart}\n'
      f'Product added to the second position: {new_item}')
