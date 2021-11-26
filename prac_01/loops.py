def a():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()


a()


def b():
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()


b()


def c():
    Number = int(input("Number of stars:"))
    for i in range(Number):
        print('*', end=' ')
    print()


c()


def d():
    Number = int(input("Number of stars:"))
    for i in range(1, Number + 1):
        print('*'* i)
    print()


d()
