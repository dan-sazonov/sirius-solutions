input()
first_set = set(map(int, input().split()))
input()
second_set = set(map(int, input().split()))

first_set ^= second_set
print(len(first_set))
print(*sorted(first_set))
