#Maru Puran
#October 24 2023
#Modify and add to prexisting code in order to better understand how conditionals work and their features, as well as how user input can play a role when using if else if and else statements.


# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter a third number: ")) #add a line asking the user to enter a third number; creates variable to hold the input asks the user prompt in quotations and stores it as an integer

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")



#add code to confirm whether the third number is bigger smaller or the same as the first number
###
if number3 > number1: #check if number3 bigger than number1
  print("Number 3 is bigger than number 1") #print message if true
elif number3 < number1: #check if number1 bigger than number3
  print("Number 1 is bigger than number 3") #print message if true
else: #both are false meaning they're equal
  print("Both numbers 1 and 3 are the same") #print message if true


#add code to confirm whether the third number is bigger smaller or the same as the second number
###
if number3 > number2: #check if number3 bigger than number2
  print("Number 3 is bigger than number 2") #print message if true
elif number3 < number2: #check if number2 bigger than number3
  print("Number 2 is bigger than number 3") #print message if true
else: #both are false meaning they're equal
  print("Both numbers 2 and 3 are the same") #print message if true
