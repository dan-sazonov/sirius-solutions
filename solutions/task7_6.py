queue = []
command = []

while 'exit' not in command:
    command = input().split()
    if 'push' in command:
        queue.append(int(command[1]))
        print('ok')
    elif 'front' in command and queue:
        print(queue[0])
    elif 'front' in command and not queue:
        print('error')
    elif 'size' in command:
        print(len(queue))
    elif 'clear' in command:
        queue.clear()
        print('ok')
    elif 'pop' in command and queue:
        print(queue.pop(0))
    elif 'pop' in command and not queue:
        print('error')
else:
    print('bye')
