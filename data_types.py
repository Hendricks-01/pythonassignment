#1. Print the type of 42, 3.14, and 'hello'
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type('hello'))   # <class 'str'>

#2. Convert a string '100' to an integer
num = ('100')
print(num)  # 100
print(type(num))  # <class 'str'>

#3. Add an integer and a float together. What is the result?
result = 5 + 2.5
print(result)          # 7.5

#4. What happens when you try to multiply a string by a number?
multiplied = 'abc' * 3
print(multiplied)      # 'abcabcabc'


#Challenge;Write a program that: ,Asks the user to enter two numbers (as strings),Converts them to integers or floats,Prints their sum and type

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Try to convert to int, if fails, convert to float
def convert(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

n1 = convert(num1)
n2 = convert(num2)

total = n1 + n2
print("Sum:", total)
print("Type of sum:", type(total))