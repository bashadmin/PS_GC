def num_text(num):
    # convert a number from 1 to 1000 to a string in the format:
    # "<something> thousand <something> hundred and <something>ty <something>"
    # if number is out of range, return -1

    # Examples:
    # 1000 returns "one thousand"
    # 956 returns "nine hundred and fifty six"
    # 318 returns "three hundred and eighteen"
    # 42 returns "forty two"
    # 1 returns "one"
    
    # might need to rename this function
    def num_name(n):
        # we will be converting the name of a single digit more than one time,
        # so make a function to do it to avoid code duplication

        # this can be improved by using a dictionary instead of multiple ifs
        if n == 1:
            return "one"
        elif n == 2:
            return "two"
        elif n == 3:
            return "three"
        elif n == 4:
            return "four"
        elif n == 5:
            return "five"
        elif n == 6:
            return "six"
        elif n == 7:
            return "seven"
        elif n == 8:
            return "eight"
        elif n == 9:
            return "nine" 
    
    if num > 1000 or num < 1:
        return -1

    # here we are splitting off the place values for the number
    # integer division to get rid of the lower digits, 
    # then modulo to get rid of the higher digits

    thousands = num // 1000
    hundreds = num // 100 % 10
    tens = num // 10 % 10
    ones = num % 10

# this was a debugging statement
#    print(thousands, hundreds, tens, ones)

# start with an empty string and build the string from highest values to lowest
    text = ""
# only add to the string if there is sonething to add
    if thousands != 0:
        text = text + num_name(thousands) + " thousand"
    if hundreds != 0:
# these <if text != "":> tests are to prevent trailing spaces
# can probably fix that with .rstrip() at the end
        if text != "":
            text = text = " "
        text = text + num_name(hundreds) + " hundred"
# the problem specifically asked for this "and"
# I personally prefer the numbers without this "and"
# like "four hundred forty four"
    if tens != 0 or ones != 0:
        if text != "":
           text = text + " and "
# tens place numbers have special names, and the teens are special too       
# using a dictionary would include these cases too
        if tens == 9:
           text = text + "ninety"
        elif tens == 8:
           text = text + "eighty"
        elif tens == 7:
           text = text + "seventy"
        elif tens == 6:
           text = text + "sixty"
        elif tens == 5:
           text = text + "fifty"
        elif tens == 4:
           text = text + "forty"
        elif tens == 3:
           text = text + "thirty"
        elif tens == 2:
           text = text + "twenty"
        elif tens == 1:
            if ones == 9:
                text = text + "ninteen"
            elif ones == 8:
                text = text + "eighteen"
            elif ones == 7:
                text = text + "seventeen"
            elif ones == 6:
                text = text + "sixteen"
            elif ones == 5:
                text = text + "fifteen"
            elif ones == 4:
                text = text + "fourteen"
            elif ones == 3:
                text = text + "thirteen"
            elif ones == 2:
                text = text + "twelve"
            elif ones == 1:
                text = text + "eleven"
            elif ones == 0:
                text = text + "ten"
# lastly, only add the ones place value name if it not in the teens
    if ones != 0 and tens != 1:
# the following conditional gave me problems because of the " and " requirement 
# adding an additional special case to handle
        if text != "" and tens > 1:
            text = text + " "
        text = text + num_name(ones)

    return(text)

# debugging test cases
for number in range(1,121):
    print(num_text(number))
print()
for number in range(190,221):
    print(num_text(number))
print()
for number in range(990,1021):
    print(num_text(number))
print()
for number in range(-5,5):
    print(num_text(number))



