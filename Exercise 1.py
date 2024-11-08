# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name =  input("Enter your name: ")
#Answer: Make sure your string text is user friendly
# TODO: Ask the user for their age and store it in a variable
age = input("Enter your age: ")
# age = int(input('Enter your name: ')) - Can add 'int' also. But its more complicated.
# - print('f')
# TODO: Print a greeting using the name and age variables
print('Hello '+ name +', age '+ age)

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter length of rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter width of rectangle: "))
# TODO: Calculate the area of the rectangle
area = (length * width)
# TODO: Print the result
print(area)
# print (f"The area is: {area}") (Can also be used)- The f statement is used because int cannot be used when dealing with strings.
#print("The area is + str(area)")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temp = float(input("Enter the temperature in celsius: "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (temp * 9/5) + 32 
# TODO: Print the result rounded to two decimal places
print(fahrenheit)
#print(f"The fahrenheit is {round(fahrenheit,2)}") - answer