
# Assignment:1, Problem:1
def max_function(num1,num2):
    if(num1>num2):
        print("Maximum number is : "+str(num1))
    else:
        print("Maximum number is : "+str(num2))

max_function(3,9)



# Assignment:1, Problem:2
def fizz_buzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

fizz_buzz(27)
fizz_buzz(25)
fizz_buzz(45)
fizz_buzz(44)



# Assignment:1, Problem:4
def odd_even(limit):
    i=0
    while(i<=limit):
        if i%2==0:
            print(str(i)+" "+"EVEN")
            i +=1
        else:
            print(str(i)+" "+"ODD")
            i+=1
odd_even(10)


# Assignment:1, Problem:6
def show_stars(rows):
    for i in range(rows+1):
        print(i*"\*")

show_stars(5)
