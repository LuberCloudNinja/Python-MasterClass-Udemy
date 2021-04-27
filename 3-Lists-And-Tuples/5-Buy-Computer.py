available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "HDMI cable",
                   "Dvd drive"
                   ]
current_choice = "-"
computer_parts = []  # create an empty list.

while current_choice != "0":
    if current_choice in "1234567":
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
        elif current_choice == "7":
            computer_parts.append("Dvd drive".casefold())
    else:
        print("Please add from the list below: ")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")

    current_choice = input("Please enter a value from the above list: ")
print(f"You added the fallowing to the list {computer_parts}: ")
