a = dict()

couple = 'a', 'b'
a[0] = couple

b = dict.fromkeys(a.values())

print(b)

for value in b:
    print(value)
    if (b[value] is not None):
        print('oui')
    else:
        print('non')