# import random module
import random

# write a random number generator function
def random_number_generator():
    return random.randint(1,20)

random_number = random_number_generator()

# welcome user and prompt user to guess the number
print("Hi. Welcome to random number generator.")

guessed_number = None

# keep asking for input until user guessed the correct number
while guessed_number!=random_number:
    # prompt user to guess a number
    guessed_number_str = input("Please enter a number between 1 and 20 : ")

    # input validation
    try:
        guessed_number = int(guessed_number_str)

        if guessed_number < 1 or guessed_number > 20:
            print("Invalid number. Please enter a number in the 1 to 20 range.")
        elif guessed_number < random_number:
            print("The entered number is too low!")
        elif guessed_number > random_number:
            print("The entered number is too high!")

    except ValueError:
        print("Invalid input. Please enter an integer number")

# end game message
print(f"Congratulations! You guessed the right number ({random_number}) ＼(^o^)／! ")