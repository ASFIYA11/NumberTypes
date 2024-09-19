n = 28  # Change this value to test other numbers
divisors_sum = sum([i for i in range(1, n) if n % i == 0])

is_perfect = divisors_sum == n
print(f"{n} is Perfect: {is_perfect}")
28 is Perfect: True
