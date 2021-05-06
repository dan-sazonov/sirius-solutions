opening = []
sign_inverse = {')': '(', ']': '[', '}': '{'}

for sign in input():
    if sign in ('(', '[', '{'):
        opening.append(sign)
    elif opening and sign_inverse[sign] != opening[-1]:
        print('no')
        break
    elif not opening:
        print('no')
        break
    else:
        opening.pop()
else:
    print('no' if opening else 'yes')
