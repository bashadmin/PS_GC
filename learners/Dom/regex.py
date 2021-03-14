#import regular expression library
import re

#get file name and open the file
fname = input("File name: ")
fh = open(fname)

#initialize total
total = 0

# find every number on each line and add them together
# "[0-9]+" matches one or more consecutive digits
for line in fh:
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        total = total + int(number)

print(total)
