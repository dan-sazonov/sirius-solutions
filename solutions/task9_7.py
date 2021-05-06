from functools import cmp_to_key

n = int(input())
a = [input() for _ in range(n)]

print(''.join(sorted(a, key=cmp_to_key(lambda x, y: -1 if x + y > y + x else x + y != y + x))))
