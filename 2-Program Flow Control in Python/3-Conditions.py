age = int((input("How old are you: ")))


def ages():
    # if age >= 16 and age <= 65:
    if 16 <= age <= 65:
        print("Have a good day at work!")
    elif age < 16:
        print("You're too young to work, but still have a nice day!")
    else:
        print("You're too old to work, but still have a nice day!")


# ages()

print("_" * 80)

# if age < 16 or age > 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

