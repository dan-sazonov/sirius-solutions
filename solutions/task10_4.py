input()
t = set(list(map(int, input().split())))
input()
r = set(list(map(int, input().split())))
input()
t1 = set(list(map(int, input().split())))
input()
r1 = set(list(map(int, input().split())))

if (t & t1) or r1 <= r:
    print(-1)
else:
    teachers = t1 | t
    print(len(teachers))
    print(*sorted(teachers))
    r.add(min(r1 - r))
    print(len(r))
    print(*sorted(r))
