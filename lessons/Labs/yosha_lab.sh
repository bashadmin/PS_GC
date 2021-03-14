#Script1
echo "Enter your name"
read name
echo "Hello,$name"


#Script3
echo "How many stars would you like to print?"
read number

for ((i = 0 ; i < $number ; i++)); do
echo "*"
done


#Script2
echo Enter first number
read num1
echo Enter second number
read num2

if [ $num1 -lt $num2 ]; then
  echo "$num1 is less than $num2"
elif [ $num2 -lt $num1 ];then
  echo "$num2 is less than $num1"
else
  echo "They are equal."
fi