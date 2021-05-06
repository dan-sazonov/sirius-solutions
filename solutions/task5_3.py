n, x = map(int, input().split())
ask = list(map(int, input().split()))
sale = list(map(int, input().split()))

ask_day = sell_day = -2
amount = x
min_a = ask[0]
min_i = 0

for i in range(n):
    if ((x // min_a) * sale[i] + x % min_a) > amount:
        amount = (x // min_a) * sale[i] + x % min_a
        ask_day = min_i
        sell_day = i
    if ask[i] < min_a:
        min_a = ask[i]
        min_i = i
else:
    print(amount)

print(ask_day + 1, sell_day + 1)
