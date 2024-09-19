import math

n = 145  # Change this value to test other numbers
sum_of_factorials = sum([math.factorial(int(d)) for d in str(n)])

is_strong = sum_of_factorials == n
print(f"{n} is Strong: {is_strong}")
145 is Strong: True
