def enter_vip_zone(available_tickets, checked_in_tickets, ticket_code, age):
    if ticket_code in available_tickets:
        if age >= 18:
            available_tickets.remove(ticket_code)
            checked_in_tickets.append(ticket_code)
            return 'ACCESS_GRANTED'
        else:
            return 'UNDERAGE'
    else:
        return 'INVALID_TICKET'

tickets = ['VIP01', 'VIP02', 'VIP03', 'VIP04']
checked = []

code_ticket = input('Enter your ticket code: ').upper().strip()
age = int(input('Enter your age: '))

updated_tickets = enter_vip_zone(tickets, checked, code_ticket, age)

formatted_tickets = ', '.join(f'{ticket}' for ticket in tickets)
formatted_checked = ', '.join(f'{ticket}' for ticket in checked)

if updated_tickets == 'ACCESS_GRANTED':
    print('Access GRANTED! Welcome to the VIP area.')
elif updated_tickets == 'UNDERAGE':
    print('Access DENIED: You must be 18 or older.')
else:
    print('Access DENIED: Invalid or already used ticket.')

print(f'Available tickets: {formatted_tickets}')
print(f'Checked-in tickets: {formatted_checked}')
