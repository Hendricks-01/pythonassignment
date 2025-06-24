# 1.write a program that checks if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2.Create a program that checks if someone is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 3.Write a program that takes 3 numbers and prints the largest one.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)

# 4. Practice combining and, or, not
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

if x > 0 and y > 0:
    print("Both x and y are positive.")
elif x > 0 or y > 0:
    print("At least one of x or y is positive.")
if not (x > 0):
    print("x is not positive.")
    
#Challenge;Build a grading system:
# Grading System
# Prompt user for input
score_input = input("Enter your score (0–100): ")

# Validate the input
if not score_input.isdigit():
    print("Please enter a valid number.")
else:
    score = int(score_input)
    if score > 100 or score < 0:
        print("Score must be between 0 and 100.")
    else:
        # Grading logic
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Your grade is: {grade}")
 
    