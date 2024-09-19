n = 12  # Change this value to test other numbers
divisors_sum = sum([i for i in range(1, n) if n % i == 0])

is_abundant = divisors_sum > n
print(f"{n} is Abundant: {is_abundant}")
12 is Abundant: True
