#Problem 1
# print('Hello, world')

# Problem 2
# import random
# display = []
# display.append(random.randrange(1, 100, 2))
# display.append(float(random.randrange(2, 101)))
# fruits = ["Cherry", "Strawberry", "Orange", "Apple", "Banana"]
# display.append(random.choice(fruits))
#
# print(
# f"Random odd number from 1-99: {display[0] : >5}",
# f"\nRandom number from 1-100: {display[1] : >8}",
# f"\nRandom fruit: {display[2] : >20}")

# Problem 3
# flower = input("Please enter the name of a flower: ")
# print(f'Name of flower: {flower}')

#Problem 4
# weather = input("Is it cloudy or sunny: ")
# print(f'It is {weather}!')

#Problem 5
# display = []
# display.append(str(input('Please enter a word: ')))
# display.append(str(input('Please enter the temperature outside: ')))
# display.append(str(input('What is your favorite fruit: ')))
# print(display)
# display.reverse()
# print(display)
# counter = 0
# for i in display:
#     print('        ' + display[counter])
#     counter += 1

#Problem 6
# sport = str(input('What is your favorite sport: '))
# print(sport)
# part = str(input('Please enter a body part: '))
# print(part)
# word = str(input('What is your favorite word: '))
# print(word)
#
# items = '$'.join([sport, part, word])
# print(items)

#Problem 7
# name = str(input('What is your name: '))
# even_num = 0
# while even_num % 2 != 0 or 2 > even_num or even_num > 100:
#     even_num = int(input('Please enter an even number between 2 and 100: '))
# decimal = ''
# while type(decimal) != float:
#     decimal = input('Please enter a decimal: ')
#     if decimal.isnumeric():
#         decimal = float(decimal)
#     elif decimal.isalpha():
#         decimal = input(('Please enter a decimal: '))
# print(name, even_num, decimal)

#Problem 8
# word = str(input('Please enter a common word: '))
# number = int(input('Please enter a number from 1-200: '))
# while number < 1 or number > 200:
#     number = int(input('Please enter a number from 1-200: '))
# decimal = float(input('Please enter a decimal: '))
# while type(decimal) != float:
#     decimal =float(input('Please enter a decimal: '))
# print(f"{word}" + '\n' + f"{number}" + '\n' + f"{decimal:.2f}")

#Problem 9
# word = input('Please enter a room in a house: ')
# number = input('Please enter an even number from 2-100: ')
# while number < 2 or number > 100 or number%2 != 0:
#     number = int(input('Please enter an even number from 2-100: '))
# decimal = input('Please enter a decimal between 1-100: ')
# while type(decimal) != float or decimal < 1 or decimal > 100:
#         decimal =float(input('Please enter a decimal between 1-100: '))
# print(f"{word}" + '\n' + f"{number}" + '\n' + f"{decimal:.2f}")
#
# word = str(word)
# number = int(number)
# decimal = float(decimal)

#Problem 10
number = int(input('Please enter an even number from 2-100: '))
while number < 2 or number > 100 or number%2 != 0:
    number = int(input('Please enter an even number from 2-100: '))
numbertwo = int(input('Please enter an even number from 1-200: '))
while numbertwo <= 0 or numbertwo >= 201:
    numbertwo = int(input('Please enter an even number from 1-200: '))

print('\n')
print('number + numbertwo = ' + str(number + numbertwo))
print('number - numbertwo = ' + str(number - numbertwo))
print('number * numbertwo = ' + str(number * numbertwo))
print('number / numbertwo = ' + str(number / numbertwo))
print('\n')
print('numbertwo + number = ' + str(numbertwo + number))
print('numbertwo - number = ' + str(numbertwo - number))
print('numbertwo * number = ' + str(numbertwo * number))
print('numbertwo / number = ' + str(numbertwo / number))




