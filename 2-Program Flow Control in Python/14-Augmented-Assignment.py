x = 23

x += 1
print(x)  # x is now 24 (23 + 1)

x -= 4
print(x)  # x is now 100 (20 * 5)

x *= 5
print(x)  # 100

x //= 4
print(x)  # x is now 25 (100 // 4) and so on...

x /= 5
print(x)  # 5.0 - note conversion from int to float

x **= 2
print(x)  # 25.0 - x still represents a float

x %= 5
print(x)  # 0.0 - 25 is exacly divisible by 5

greeting = "Good"

greeting += " Morning"
print(greeting)

greeting *= 5
print(greeting)
