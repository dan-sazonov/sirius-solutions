from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print('YES' if is_prime(int(input())) else 'NO')
