a = 220  # Change this value to test other numbers
b = 284  # Change this value to test other numbers

sum_a = sum([i for i in range(1, a) if a % i == 0])
sum_b = sum([i for i in range(1, b) if b % i == 0])

is_amicable = sum_a == b and sum_b == a
print(f"({a}, {b}) are Amicable: {is_amicable}")
(220, 284) are Amicable: True
