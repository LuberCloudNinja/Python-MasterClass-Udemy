def game():
    available_exits = ["north", "south", "east", "west"]
    chosen_exit = ""

    while chosen_exit not in available_exits:
        chosen_exit = input("Please chose a direction: ").casefold()
        if chosen_exit.casefold() == "quit":
            print("Game over!!!")
            break
    print("Aren't you glad you got out of there")


game()
