_, distance = map(int, input().split())
cells = list(map(int, input().split()))
max_a = max_a_i = max_sum = 0
answer = 0

for a_i, a in enumerate(cells[:-distance - 1]):
    b_i = a_i + distance + 1
    b = cells[b_i]
    if a > max_a:
        max_a = a
        max_a_i = a_i
    if max_a + b > max_sum:
        max_sum = max_a + b
        answer = (max_a_i, b_i)

print(answer[0] + 1, answer[1] + 1)
