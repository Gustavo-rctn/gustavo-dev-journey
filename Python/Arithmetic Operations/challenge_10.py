number = int(input('Enter an integer: '))

successor = number + 1
remainder = number % 2


print(f'The number entered was {number}, its successor is {successor}.')
print(f'The remainder of dividing this number by 2 is: {remainder}')


if remainder == 0:
    print('This number is Even.')
else:
    print('This number is Odd.')
