def register_client(client_list, client_name):
    client_list.append(client_name)
    return client_list

client_names = ['João', 'Gustavo', 'Guilherme']

new_client = input('Enter the new client name: ').strip()
updated_clients = register_client(client_names, new_client)

print(f'Client list: {client_names}\n'
      f'Client added: {new_client}\n'
      f'Updated client list: {updated_clients}')
