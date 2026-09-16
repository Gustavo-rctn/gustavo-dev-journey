def log_temperature(temp_list, new_temp):
    temp_list.append(new_temp)
    return temp_list

temp_list = [22, 30, 19, 10]

new_temperature = int(input('Enter the new temperature log: '))

updated_temps = log_temperature(temp_list, new_temperature)
formatted_temps = ", ".join(f'{temp}°C' for temp in updated_temps)

print(f'Temperature update: {formatted_temps}\n')
