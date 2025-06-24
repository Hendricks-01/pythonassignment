#1. Use a for loop to print numbers from 1 to 10
for i in range(1, 11):
    print(i)

#2.Use a while loop to print numbers until the user enters 'stop'
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input.lower() == 'stop':
        break
    print(user_input)

#3.write a loop to print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Explanation:
# 'break' is used to exit a loop immediately, even if the loop condition is still true.
# 'continue' skips the rest of the current loop iteration and moves to the next iteration.


#Challenge;Write a guessing game that asks the user to guess a secret number between 1 and 10.Give feedback (too high / too low),Use a while loop.
import random
secret_number = random.randint(1, 10)
while True:
    guess = input("Guess the secret number (1-10): ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < secret_number:
        print("Too low!guess 0 to exit the game.")
    elif guess > secret_number:
        print("Too high!guess 0 to exit the game.")
    else:
        print("Congratulations! You guessed it.")
        break
        # Allow user to exit the game
    if guess == 0:
        print("Game exited.")
        break
        