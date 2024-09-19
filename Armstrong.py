n = 153  # Change this value to test other numbers
digits = [int(d) for d in str(n)]
power = len(digits)
sum_of_powers = sum([d ** power for d in digits])

is_armstrong = sum_of_powers == n
print(f"{n} is Armstrong: {is_armstrong}")
153 is Armstrong: True
