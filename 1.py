mini=1000000010000
k=0
z=0
print('Введите размер массива')
try:
    razmer = int(input())
except ValueError:
    print('ошибка ввода')
else:
    if razmer <= 0:
        print('ошибка ввода')
        exit()
    print('Введите массив')
    A = [0] * razmer
    for i in range(razmer):
        try:
            z = float(input())
        except ValueError:
            print('ошибка ввода')
            exit()
        else:
            A[i] = z 
    print('Введите DELTA')
    try:
        delta = float(input())
    except ValueError:
        print('ошибка ввода')
    else:
        for i in range(razmer):
            if A[i] < mini:
                mini = A[i]
        for i in range(razmer):
            if (A[i] + delta == mini) or (A[i] - delta == mini):
                k += 1
        print('Количество элементов, отличающихся от минимального на', delta, 'равно',k)
