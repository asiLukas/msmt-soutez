def bumbac():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('bumbác', end=', ')
        elif i % 5 == 0:
            print('bác', end=', ')
        elif i % 3 == 0:
            print('bum', end=', ')
        else:
            print(i, end=', ')

bumbac()
