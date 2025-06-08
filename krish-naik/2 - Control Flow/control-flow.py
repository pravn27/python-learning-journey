# determine if the year is a leap year or not
"""
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
"""

# Simple calculator program, take user input numbers and operator

"""
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
"""

# Determine the ticket price based on age and whether the person is a student.
# Ticket pricing based on age and student status

'''
age = int(input("Enter your age:"))
is_student = input("Are you a student ? (yes/no):").lower()

if (age < 5):
    price = "Free"
elif (age <= 12):
    price = "$10"
elif age <= 17:
    if is_student == "yes":
        price = "$12"
    else:
        price = "$20"
elif age <= 64:
    if is_student == "yes":
        price = "$18"
    else:
        price = "$25"
else:
    price = "$20"

print("Ticket price is: ", price)
'''

# Examples - Calculate the sum of first N natural numbers using a while and for loop
# using while loop
# for n = 5, the sum should be 1 + 2 + 3 + 4 + 5 = 15

input_number = int(input("Enter number"))

if (input_number > 0):
    sum = 0
    count = 1
    # with while loop
    while (count <= input_number):
        sum = sum + count
        count = count + 1

    # with for loop
    # for count in range(1, input_number + 1):
    #     sum = sum + count

    print(f"Sum of first {input_number} natural number is {sum}")
else:
    print("Please enter a positive number")
