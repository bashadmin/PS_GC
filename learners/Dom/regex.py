#import regular expression library
import re, os

#get file name and open the file
#fname = input("Please enter the name of the file: ")
with open(os.listdir()[1], 'r') as fh:
    data = fh.read()
#initialize total
total = 0

# find every number on each line and add them together
# "[0-9]+" matches one or more consecutive digits
for line in data:
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        total = total + int(number)

print(total)