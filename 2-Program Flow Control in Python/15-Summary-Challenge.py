def menu():
    print("Please chose your option from the list below: ")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo swimming")
    print("4:\tHave dinner")
    print("5:\tGo to bed")
    print("0:\tExit")


menu()

while True:
    choice = input("Please enter a number from the above menu: ")

    if choice == "0":
        print("Have a wonderful day! :)")
        break
    elif choice in "12345":
        print(f"You chose {choice}")
        break
    else:
        print("Your choice was invalid, please try entering a valid option again")
        menu()
