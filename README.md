# python_work
Python tasks
#Numpy task 1
number = []

print('Enter 4 numbers')

numbers.append(input('1=>'))
numbers.append(input('2=>'))
numbers.append(input('3=>'))
numbers.append(input('4=>'))

file = open('numbers.txt', 'w')
for number in numbers:
    file.write(number+"\n")
