string = input().split()
operands = []

for i in string:
    if i.isdigit():
        operands.append(i)
    else:
        exp = operands.pop(-2) + i + operands.pop(-1)
        operands.append(str(eval(exp)))

print(*operands)
