command = []
deque = []

while command != ['exit']:
    command = input().split()
    if command[0] == 'push_front':
        deque.insert(0, command[1])
        print('ok')
    elif command[0] == 'push_back':
        deque.append(command[1])
        print('ok')
    elif command[0] == 'pop_front':
        print(deque.pop(0) if deque else 'error')
    elif command[0] == 'pop_back':
        print(deque.pop(-1) if deque else 'error')
    elif command[0] == 'front':
        print(deque[0] if deque else 'error')
    elif command[0] == 'back':
        print(deque[-1] if deque else 'error')
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'clear':
        deque.clear()
        print('ok')
else:
    print('bye')
