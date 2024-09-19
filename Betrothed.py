a = 48  # Change this value to test other numbers
b = 75  # Change this value to test other numbers

sum_a = sum([i for i in range(1, a) if a % i == 0])
sum_b = sum([i for i in range(1, b) if b % i == 0])

is_betrothed = sum_a == b + 1 and sum_b == a + 1
print(f"({a}, {b}) are Betrothed: {is_betrothed}")
(48, 75) are Betrothed: True
