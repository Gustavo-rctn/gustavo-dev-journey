def validate_and_register_ticket(available_tickets, ticket_code, checked_in_tickets):
    if ticket_code in available_tickets:
        available_tickets.remove(ticket_code)
        checked_in_tickets.append(ticket_code)
        return True
    else:
        return False


available_tickets = ['VIP101', 'VIP102', 'VIP103', 'REG201', 'REG202']
checked_in_tickets = []

code_input = input('Enter your ticket code: ').upper().strip()

is_valid = validate_and_register_ticket(available_tickets, code_input, checked_in_tickets)

if is_valid:
    print('Access granted! Enjoy the show!')
else:
    print('Invalid or already used ticket!')

print(f'Remaining available tickets: {available_tickets}')
print(f'Checked-in tickets: {checked_in_tickets}')
