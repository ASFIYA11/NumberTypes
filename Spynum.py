n = 1124  # Change this value to test other numbers
digits = [int(digit) for digit in str(n)]
sum_digits = sum(digits)
product_digits = 1
for digit in digits:
    product_digits *= digit

is_spy = sum_digits == product_digits
print(f"{n} is Spy: {is_spy}")
1124 is Spy: True
