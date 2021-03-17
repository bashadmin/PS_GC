import os
import datetime

# Create a file, get its timestamp and print it out in a user understandable format

def file_date(filename):

  # Create the file in the current directory

  # I think 
  # 	file = open(filename, "w")
  # 	file.close() 
  # should work too

  with open(filename, "w") as file:
    pass

  # Get time when file was modified
  timestamp = os.path.getmtime(filename)

  # Convert the timestamp into a readable format, then into a string
  ti = datetime.datetime.fromtimestamp(timestamp)

  # I had a difficult time figuring out how to convert a datetime type into a string
  # I probably missed something simple.
  # It made more sense to me to access the class attributes directly, and convert them to strings

  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  
  # if i could have figured out the above portion then it would be
  # some_string[:9]

  # instead I just did this. 
  # f-strings would work too.
  # .format method syntax comes easier to me, because C

  return  "{}-{}-{}".format(str(ti.year), str(ti.month), str(ti.day))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd