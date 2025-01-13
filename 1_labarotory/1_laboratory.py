def f1():
    n = int(input("Введите число: "))
    for i in range(1, n+1):
        print(i)


def f2():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a > b:
        print(f"Большее число {a}")
    else:
        print(f"Большее число {b}")


f1()
f2()