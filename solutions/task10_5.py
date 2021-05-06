def deposit(name, amount):
    bank[name] = bank.get(name, 0) + int(amount)


def withdraw(name, amount):
    bank[name] = bank.get(name, 0) - int(amount)


def balance(name):
    log.append(bank[name] if name in bank else 'ERROR')


def income(percent):
    for i, j in bank.items():
        if j > 0:
            bank[i] = int(j * ((int(percent) / 100) + 1))


def transfer(name1, name2, amount):
    bank[name1] = bank.get(name1, 0) - int(amount)
    bank[name2] = bank.get(name2, 0) + int(amount)


bank = dict()
log = []
for _ in range(int(input())):
    line = input().split()
    if 'BALANCE' in line:
        balance(line[1])
    elif 'DEPOSIT' in line:
        deposit(line[1], line[2])
    elif 'WITHDRAW' in line:
        withdraw(line[1], line[2])
    elif 'INCOME' in line:
        income(line[1])
    elif 'TRANSFER' in line:
        transfer(*line[1:])
    else:
        withdraw(line[1], line[3])
        deposit(line[2], line[3])
print(*log, sep='\n')
