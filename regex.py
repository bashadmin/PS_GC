import re

fh = open("regex_sum_42.txt")

for line in fh:
    numbers = re.findall([0-9]+, line)
    print(numbers)
