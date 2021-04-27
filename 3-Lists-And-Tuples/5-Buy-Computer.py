available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "HDMI cable",
                   "Dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)] Will be cover in later sessions
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list.

while current_choice != "0":
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add from the list below: ")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")

    current_choice = input("Please enter a value from the above list: ")

print(f"You added the fallowing to the list {computer_parts}: ")

