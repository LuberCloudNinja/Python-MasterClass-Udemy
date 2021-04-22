shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "Spam".casefold():
        continue
    print("Buy " + item)

