def find_divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
        i += 1
    while i >= 1:
        if n % i == 0 and i != (n//i):
            print(n//i)
        i -= 1