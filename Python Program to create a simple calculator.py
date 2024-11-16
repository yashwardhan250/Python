#Python Program to create a simple calculator

#3 steps to build a calculator program
#First step functions for operations
#Second step user input
#Third step print result

#Function to add 2 no
def add(num1,num2):
    return num1+num2

#Function to subtract 2 no
def subtract(num1,num2):
    return num1-num2

#Function to multiply 2 no
def multiply(num1,num2):
    return num1*num2

#Function to divide 2 no
def divide(num1,num2):
    return num1/num2

#Function to avg 2 no
def avg(num1,num2):
    return (num1+num2)/2

#Step 2
print("Please select a operation:\n  "\
      "1. Add\n"\
      "2. Subtract\n"\
      "3. Multiply\n"\
      "4. Divide\n"\
      "5. Average")

select =int(input('Select a opertaion from 1 to 5: '))
number1 = int(input("Enter first no. : "))
number2 = int(input("Enter second no. : "))   

#Step 3
if select == 1:
    print("Sum of two no is: ",\
          add(number1,number2))
elif select ==2:
    print("Subtraction of 2 no: ",\
          subtract(number1,number2))
elif select == 3:
    print("Multiplication of 2 no: ",
          multiply(number1,number2))
elif select ==4:
    print("Division of 2 no is: ",\
          divide(number1,number2))
elif select == 5:
    print("Average of 22 no is: ",\
      avg(number1,number2))
else:
    print("Invalid operation")


    




