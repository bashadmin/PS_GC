# Student: Domenic Campochiaro
# study session work from 6 March 2021

# problem 1: variable and basic I/O 
# Prompt the user for input, store it in a variable, and display it back to them
echo "What is your name, user?"
read name
echo "Hello, $name"

# problem 2: using conditionals
# Prompt for input, and diplay output based on user's response
# demonstrating if...elif...else structure
echo
echo "$name, you find yourself in a white room with two doors, red and black."
echo "Which door whould like to enter?"

read door

if [ $door == "red" ]; then
    echo "You are in a $door room, $name."
elif [ $door == "black" ]; then
    echo "$name, you have entered a $door room."
else
    echo "There is no $door door, $name."
fi

echo
echo "Let us draw a square. How big should the sides be?"

read side

if [[ $side -lt 20 ]]; then
for ((i = 0; i < $side; i++)); do
   for ((j = 0; j < $side; j++)); do
       echo -n "#"
   done
   echo
done
else
echo "That square would be too big."
fi

echo
echo "Let us calculate the surface area of a box."

echo -n "Enter the the length: "
read -r length
echo -n "Enter the width: "
read -r width
echo -n "Enter the height: "
read -r height

surface_area() {
    s_a=$((2*length*width+2*length*height+2*width*height))
    echo "The surface area is $s_a."
    }

surface_area

echo
echo "cmds.txt contains a list of the commands in /usr/bin"
echo "Put names of bash scripts in sh.txt, and python scripts in py.txt"

choice="x"
while !(choice == "x" && choice == "y"); do
echo "Do you want to see which scripts are being stored? [y/n]: "
read choice
done
echo

show=[[choice == "x" && choice == "y"]]

file="./cmds.txt"

while read -r line; do
    if [[ $line =~ \.sh$ ]]; then
        echo "$line --> sh.txt"
        echo $line >> sh.txt
    elif [[ $line =~ \.py$ ]]; then
        echo "$line --> py.txt"
        echo $line >> py.txt
    fi
    
done < $file
