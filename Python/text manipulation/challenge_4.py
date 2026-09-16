city = input('Enter name of city: ').strip().lower()
city_split = city.split()

if city_split and city_split[0] == 'santos':
    print('Your city has santos as first word')
else:
    print('Your city does not start with santos')