# determine if the year is a leap year or not
'''
year = int(input("Enter a year"))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year")
        else: 
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
'''

# Simple calculator program, take user input numbers and operator

'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if (operator == "+"):
    result =  num1 + num2
elif (operator == "-"):
    result =  num1 - num2
elif (operator == "*"):
    result =  num1 * num2
elif (operator == "/"):
    if num2 != 0:
        result =  num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"

print("Result:", result)
'''

# Determine the ticket price based on age and whether the person is a student.
# Ticket pricing based on age and student status

age = int(input("Enter your age:"))
is_student = input("Are you a student ? (yes/no):").lower()

if (age < 5):
    price = 'Free'
elif (age <= 12):
    price = '$10'
elif (age <= 17):
    if (is_student == 'yes'):
        price = '$12'
    else:
        price = '$20'
elif (age <= 64):
    if (is_student == 'yes'):
        price = '$18'
    else:
        price = '$25'
else: 
    price = '$20'

print("Ticket price is: ", price)