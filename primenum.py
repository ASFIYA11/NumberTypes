n = 29  # Change this value to test other numbers
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print(f"{n} is Prime: {is_prime}")
29 is Prime: True
