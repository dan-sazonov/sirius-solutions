first_pack = input().split()
second_pack = input().split()
move_counter = 0

while first_pack and second_pack:
    move_counter += 1
    a, b = first_pack.pop(0), second_pack.pop(0)
    if a > b and (a, b) != ('9', '0') or (a, b) == ('0', '9'):
        first_pack.extend([a, b])
    else:
        second_pack.extend([a, b])
    if move_counter >= 10 ** 6:
        print('botva')
        break
else:
    print('first' if first_pack else 'second', move_counter)
