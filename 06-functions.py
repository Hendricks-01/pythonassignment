#1.Write a function greet(name) that prints “Hello, [name]”.
def greet(name):
    print(f"Hello, {name}")


#2.Create a function add(a, b) that returns the sum of a and b, and prints "even" if the result is even, or "odd" if the result is odd.
def add(a, b):
    result = a + b
    if result % 2 == 0:
        print("even")
    else:
        print("odd")
    return result

#4.Call a function from within another function.
def greet_and_add(name, a, b):
    greet(name)
    sum_result = add(a, b)
    print(f"The sum is: {sum_result}")

#Challenge;Write a calculator function,Takes two numbers and an operation (+, -, *, /),Returns the result
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"   
    
result = calculator(10, 5, '+')
print("Result:", result)    #testing the calculator function
