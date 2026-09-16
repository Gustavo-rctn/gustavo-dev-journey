def add_vip_client(queue, client_name):
    queue.insert(0, client_name)
    return queue

bank_queue = ['Carlos', 'Ana']
name_client = input('Enter the VIP client name: ').strip()

updated_queue = add_vip_client(bank_queue, name_client)
formatted_queue = ", ".join(f'{name}' for name in updated_queue)

print(f'VIP client name: {name_client}\n'
      f'Queue status: {formatted_queue}')
