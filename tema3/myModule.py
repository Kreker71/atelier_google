def f1(n):
    if n <= 1:
        return n
    else:
        return n + f1(n - 1)

def sum_even_0_to_n(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return sum_even_0_to_n(n-2) + n
    else:
        return sum_even_0_to_n(n-1)

def sum_odd_0_to_n(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return sum_even_0_to_n(n-2) + n
    else:
        return sum_even_0_to_n(n-1)

print(sum_odd_0_to_n(5))
print((sum_even_0_to_n(5)))