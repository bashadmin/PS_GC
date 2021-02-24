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
# display.append(str(input('Please, enter a word: ')))
# display.append(str(input('Please, enter the temperature outside: ')))
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
# part = str(input('Please, enter a body part: '))
# print(part)
# word = str(input('What is your favorite word: '))
# print(word)
#
# items = '$'.join([sport, part, word])
# print(items)

#Problem 7
# name = str(input('What is your name: '))
# even_num = int(input('Please, enter an even number between 2 and 100: '))
# while even_num % 2 != 0 or 2 > even_num or even_num > 100:
#     even_num = int(input('Please, enter an even number between 2 and 100: '))
# decimal = ''
# while type(decimal) != float:
#     decimal = input('Please, enter a decimal: ')
#     if decimal.isnumeric():
#         decimal = float(decimal)
#     elif decimal.isalpha():
#         decimal = input(('Please, enter a decimal: '))
# print(name, even_num, decimal)


