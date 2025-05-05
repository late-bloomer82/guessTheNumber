# import random module
import random

# write a random number generator function
def random_number_generator():
    return random.randint(1,20)

random_number = random_number_generator()

# welcome user and prompt user to guess the number
print("Hi. Welcome to random number generator.")

guessed_number_str = input("Guess a random number between 1 and 20 inclusive: ")
guessed_number = int(guessed_number_str)

if guessed_number<1 or guessed_number>20:
    print("Invalid number. Please enter a number in the 1 to 20 range.")

if guessed_number != int:
    print("Invalid input. Please enter a number")

