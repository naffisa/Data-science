num1 = int(input('enter first number:'))
num2 =int(input('enter second number:'))

print('enter which operation would you like to perform?')
number = input("press'a' if you want to add\npress 'b' if you want to subtract\npress 'c' if you want to multiply\npress 'd' if you want to divide:")
if number == 'a':
    result = num1 + num2
elif number == 'b':
    result = num1 - num2
elif number == 'c':
    result = num1 * num2
elif number== 'd':
    result = num1 / num2
else:
    print('input character is not recognised!')

if number == 'a':
    print(num1, '+', num2, ':', result)
elif number == 'b':
    print(num1, '-', num2, ':', result)
elif number == 'c':
    print(num1, '*', num2, ':', result)
elif number == 'd':
    print(num1, '/', num2, ':', result)
else:
    print('input character is not recognised!')