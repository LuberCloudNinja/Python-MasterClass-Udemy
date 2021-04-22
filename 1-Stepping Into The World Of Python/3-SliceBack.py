letters = "abcdefghijklmnopqrstuvwxyz"

backwards1 = letters[25::-1]
backwards2 = letters[::-1]
print(backwards1)
print(backwards2)

print(letters[16::-1][0:3])
print(letters[4::-1])
print(letters[18::][::-1])

print(letters[-4:])  # Returns the last four items of the string.
print(letters[-1:])  # Returns the last item of the string.


