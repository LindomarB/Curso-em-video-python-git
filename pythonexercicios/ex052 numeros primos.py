num = int(input('digite um valor: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m ', c, end=' ')
        tot += 1
    else:
        print('\33[31m', c, end=' ')
if tot ==2:
    print('\033[m e primo')
else:
    print('\033[m nao e primo')
