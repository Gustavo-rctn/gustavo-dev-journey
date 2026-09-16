# The street speed limit is 60 km/h
# This program simulates a traffic radar
# If the driver exceeds the limit, a fine is calculated proportionally to the excess speed

current_speed = float(input('Enter the car speed (km/h): '))

# Calculate the speed excess (how much over the limit the driver was)
speed_excess = current_speed - 60.0

# Formula logic: Base excess plus a proportional multiplier
fine_amount = speed_excess + (7.0 * speed_excess)

if current_speed <= 60.0:
    print('Speed within the limit. Have a safe trip!')
else:
    print(f'You have been fined! The total ticket amount is ${fine_amount:.2f}')
