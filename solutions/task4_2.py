def find_div(n=int(input())):
    i = 2
    while n >= i ** 2:
        if not n % i:
            return i
        i += 1
    return n


print(find_div())
