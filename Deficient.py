n = 15  # Change this value to test other numbers
divisors_sum = sum([i for i in range(1, n) if n % i == 0])

is_deficient = divisors_sum < n
print(f"{n} is Deficient: {is_deficient}")
15 is Deficient: True
