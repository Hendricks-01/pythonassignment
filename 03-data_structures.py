#1 Create a list of fruits and print the third fruit
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("The third fruit is:", fruits[2])

#2.create a dictionary with keys: name, age
person = {'name': 'Alice', 'age': 30}
print("The value of age is:", person['age'])

#3.Define a tuple with three numbers.Try modifying it. What happens?
numbers = (1, 2, 3)
#try:
    #numbers[0] = 10  # Attempt to modify tuple, this will raise an error if uncommented
#you get a TypeError because tuples are immutable.
    



#4. Set from a list with duplicate values
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Set with unique values:", unique_numbers)

# Challenge Create a program that:, Takes 5 user inputs and stores them in a list, Converts the list into a set and prints the unique values
user_inputs = []
for i in range(5):
    value = input(f"Enter value {i+1}: ")
    user_inputs.append(value)

# Convert the list into a set and print unique values
unique_inputs = set(user_inputs)
print("Unique values entered:", unique_inputs)
