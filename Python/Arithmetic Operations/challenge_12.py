total_seconds = int(input('Digite o total em segundos:'))
hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
remaining_seconds = total_seconds % 3600 % 60

print('\nConversion result:')
print(f'Hours: {hours}')
print(f'Minutes: {minutes}')
print(f'Seconds: {remaining_seconds}')
print(f'({total_seconds} seconds is equal to {hours}h {minutes}m {remaining_seconds}s)')