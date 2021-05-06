stack = []
command = ''

while command != 'exit':
    command = input()
    if command.split()[0] == 'push':
        stack.append(command.split()[1])
        print('ok')
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        stack.clear()
        print('ok')
    try:
        if command == 'pop':
            print(stack.pop())
        elif command == 'back':
            print(stack[-1])
    except IndexError:
        print('error')
else:
    print('bye')
