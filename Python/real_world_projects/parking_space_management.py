def park_car(available_spots, occupied_spots, spot_code):
    if spot_code in available_spots:
        available_spots.remove(spot_code)
        occupied_spots.append(spot_code)
        return True
    else:
        return False

available = ['ABC-1234', 'XYZ-9999', 'KDM-5544']
occupied = []

spot_input = input('Enter the parking spot code: ').upper().strip()
update_parking = park_car(available, occupied, spot_input)

if update_parking:
    print('Parking spot available!')
else:
    print('Parking spot unavailable!')

formatted_free = ', '.join(f'{spot}' for spot in available)
formatted_occupied = ', '.join(f'{spot}' for spot in occupied)

print(f'Free spots: {formatted_free}')
print(f'Occupied spots: {formatted_occupied}')
