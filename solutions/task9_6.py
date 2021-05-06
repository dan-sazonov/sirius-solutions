n = int(input())
print(*(sorted(list(map(int, input().split())), key=lambda x: sum(map(int, str(x))), reverse=True)))
