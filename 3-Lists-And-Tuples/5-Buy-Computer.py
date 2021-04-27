current_choice = "-"
computer_parts = []  # create an empty list.

while current_choice != "0":
    if current_choice in "123456":
        print(f"Adding {current_choice}")
        if current_choice == "1":
            computer_parts.append("Computer".casefold())
        elif current_choice == "2":
            computer_parts.append("Monitor".casefold())
        elif current_choice == "3":
            computer_parts.append("Keyboard".casefold())
        elif current_choice == "4":
            computer_parts.append("Mouse".casefold())
        elif current_choice == "5":
            computer_parts.append("Mouse mat".casefold())
        elif current_choice == "6":
            computer_parts.append("HDMI cable".casefold())

    else:
        print("Please add from the list below: ")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Mouse mat")
        print("6: HDMI cable")
        print("0: To finish")

    current_choice = input("Please enter a value from the above list: ")
print(f"You added the fallowing to the list {computer_parts}: ")
