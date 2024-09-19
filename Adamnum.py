n = 12  # Change this value to test other numbers
rev_n = int(str(n)[::-1])

is_adam = n**2 == int(str(rev_n**2)[::-1])
print(f"{n} is Adam: {is_adam}")
12 is Adam: True

