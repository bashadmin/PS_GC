# def max_number(number_one,number_two):
#     if number_one > number_two:
#         return number_one
#     else:
#         return number_two
#
# print(max_number(1,2))

# def fizz_buzz(number):
#     if number%3 == 0 and number%5 != 0:
#         return "Fizz"
#     elif number%5 == 0 and number%3 != 0:
#         return "Buzz"
#     elif number%5 == 0 and number%3 == 0:
#         return "FizzBuzz"
#     else:
#         return number
#
# print(fizz_buzz(9))
# print(fizz_buzz(25))
# print(fizz_buzz(15))
# print(fizz_buzz(8))

# def speed_check(speed):
#     if speed <= 70:
#         print("OK")
#     elif speed > 70:
#         demerit = 0
#         demerit = (speed - 70)//5
#         if demerit > 12:
#             print("License suspended!")
#         else:
#             print("Points: " + str(demerit))
#
# speed_check(50)
# speed_check(70)
# speed_check(90)
# speed_check(9000)

# def showNumbers(limit):
#     for i in range(limit+1):
#         if i%2 == 0 or i == 0:
#             print(str(i) + " EVEN")
#         else:
#             print(str(i) + " ODD")
#
# showNumbers(5)
# print("----------")
# showNumbers(10)

# def multiples(limit):
#     sum = 0
#     for i in range(limit+1):
#         if i%3 == 0 or i%5 == 0:
#             sum += i
#     return sum
#
# print(multiples(7))
# print(multiples(20))

# def show_stars(rows):
#     for i in range(rows+1):
#         print(i*"*")
#
# show_stars(9)

def prime(limit):
    for i in range(limit + 1):
        if i in {2, 3, 5, 7}:
            print(str(i))
        elif i > 10 and i%2 != 0 and  i%3 != 0 and 1%5 != 0 and i%7 !=0:
            print(str(i))

prime(9)
print("-----")
prime(20)
print("-----")
prime(50)








