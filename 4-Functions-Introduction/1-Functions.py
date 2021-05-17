def multiply(x, y):
    """

    :param x: Integer value
    :param y: Integer value
    :return: Returns to user the multiplication of x & y values.
    """
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome")

answer = multiply(18, 3)
print(answer)
