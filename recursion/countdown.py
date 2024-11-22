def count_down1(n):
    for i in range(n):
        print(n - i)


def count_down2(n):
    for i in range(n, 0, -1):
        print(i)

def count_down3(n):
    while n >= 1:
        print(n)
        n = n - 1

def count_down4(n):
    if n == 0:
        print("Countdown complete")
    elif n > 0:
        print(n)
        count_down4(n - 1)


def print_n(str, n):
    if n == 0:
        print()
    elif n > 0:
        print(str)
        print_n(str, n-1)

print_n("Go Birds", 5)