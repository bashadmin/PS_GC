num_dict = {
    0:"",
    10:"ten",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",
    11:"eleven",12:"twelve",13:"fhirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
    19:"nineteen", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
    100:"one hundred",1000:"one thousand"
    }
text = ""
def num_to_str(number):
    if (len(str(number)) > 4) or (number > 1000):
        return print('-1')
    # elif number == 1000:
    #     print("one thousand")
    elif number in num_dict:
        return print(num_dict[number])
    try:
        num_string = str(number)
        num_length = len(num_string)
        if num_length == 3:
            text = print(f'{num_dict[int(num_string[0])]} hundred and {num_dict[int(num_string[1:3]) - int(num_string[-1])]} {num_dict[int(num_string[-1])]}')
            return text
        if num_length == 2:
                text = print(f'{num_dict[int(num_string)]}')
    except:
        print('failed')
num_to_str(1000)
num_to_str(1001)
num_to_str(10001)
num_to_str(999)
num_to_str(223)
num_to_str(15)
num_to_str(1)
num_to_str(45)
num_to_str(125)



def fizzBuzz(n):
    try:
        int(n)
        for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz")
            elif (i % 3 == 0) and (i % 5 != 0):
                print("Fizz")
            elif (i % 5 == 0) and (i % 3 != 0):
                print("Buzz")
            elif (i % 3 != 0) and (i % 5 != 0):
                print(i)
    except:
        print("You did not enter a valid integer")