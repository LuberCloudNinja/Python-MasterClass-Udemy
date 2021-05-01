import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f"{temp} is not a valid number.")


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0  # Initialise to any number that doesn't equal the answer.
print(f"Please guess number between 1 and {highest}: ")

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    elif guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print("Please guess higher.")
        else:  # guess must be greater than answer.
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly.")
