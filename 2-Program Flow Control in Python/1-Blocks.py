# for i in range(1, 13):
#     print(f"No. {1} squared us {i ** 2} and cubed is {i ** 3}")
#     print("*" * 80)


name = input("Please enter your name: ")
age = int(input("How old are you?: "))

# if age >= 18:
#     print("You're old enough to vote")
#     print("Please put an X in the box.")
# elif age == 17:
#     print(print(f"Please come back in {18 - age} year!"))
# else:
#     print(f"Please come back in {18 - age} years!")

if age < 18:
    print(f"Please come back in {18 - age} year!")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi.")
else:
    print("You're old enough to vote")
    print("Please put an X in the box.")
