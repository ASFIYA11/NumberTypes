n = 19  # Change this value to test other numbers

while n > 9:
    n = sum([int(digit) for digit in str(n)])

is_magic = (n == 1)
print(f"{n} is Magic: {is_magic}")
1 is Magic: True
