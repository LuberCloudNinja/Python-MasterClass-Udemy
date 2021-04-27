even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)
print()
even.sort()
print(even)
even.sort(reverse=True)
print(even)
print(another_even)