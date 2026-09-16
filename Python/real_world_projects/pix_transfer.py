def send_pix(registered_keys, client_balance, destination_key, amount, face_id_verified):
    if destination_key not in registered_keys:
        return 'INVALID_KEY'
    elif amount > 1000:
        return 'LIMIT_EXCEEDED'
    elif client_balance < amount:
        return 'INSUFFICIENT_FUNDS'
    elif not face_id_verified:
        return 'FACE_ID_NOT_RECOGNIZED'
    else:
        return client_balance - amount  # new client balance

# Application data
valid_keys = ["user1@email.com", "11999998888", "333.222.111-00"]  # registered keys
my_balance = 2500.0
my_face = True

# Terminal inputs
key_input = input("Enter the destination PIX key: ").strip()
pix_value = float(input("Enter the PIX amount: $ "))

# Call function and handle the 4 scenarios
update_pix = send_pix(valid_keys, my_balance, key_input, pix_value, my_face)

if update_pix == "INVALID_KEY":
    print('The entered key is INVALID!')
elif update_pix == "LIMIT_EXCEEDED":
    print('Transaction LIMIT EXCEEDED! Maximum allowed per transfer is $1000.')
elif update_pix == "INSUFFICIENT_FUNDS":
    print('Your balance is INSUFFICIENT!')
elif update_pix == "FACE_ID_NOT_RECOGNIZED":
    print(f'Face ID verification failed: {my_face}')
else:
    print('PIX transfer successful!')
    print(f'Your new balance is: ${update_pix:.2f}')
