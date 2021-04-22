parrot = "Norwegian Blue"

print(parrot)

print(parrot[3].title())
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print(parrot)

print(parrot[-1])
print(parrot[-14])

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian or:
print(parrot[:9])  # Norwegian
print(parrot[10:14])  # Blue or:
print(parrot[10:])
print(parrot)
print()
print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:])  # Norwegian Blue
print()
""" Negative Slicing """

print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl
print(parrot[-14:8])  # Bl

""" Steps and sclicing """
# Norwegian Blue
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
