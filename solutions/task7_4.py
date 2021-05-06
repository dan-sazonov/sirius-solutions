input()
cars = list(map(int, input().split()))
cars_amount = len(cars)

cars = cars[::-1]
temp, res = [], []
track_1, track_2 = [0], [0]

while True:
    temp.append(cars.pop())
    while temp and cars and temp[-1] == cars[-1] + 1:
        temp.append(cars.pop())
    if track_2 and cars and track_2[-1] + 1 == cars[-1]:
        temp.append(cars.pop())
    res.append((1, len(temp)))
    track_1.extend(temp)
    temp = []
    if track_2[-1] + 1 == track_1[-1]:
        temp.append(track_1.pop())
        while temp[-1] + 1 == track_1[-1]:
            temp.append(track_1.pop())
    if temp:
        res.append((2, len(temp)))
        track_2.extend(temp)
        temp = []
    if not cars:
        if temp:
            res.append((2, len(temp)))
            track_2.extend(temp)
        track_2.pop(0)
        if track_2 != list(range(1, cars_amount + 1)):
            res = 0
        break

if not res:
    print(0)
else:
    for a in res:
        print(*a)
