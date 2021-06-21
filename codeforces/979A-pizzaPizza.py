n = int(input())


def pizzaCuts(n):
    if n == 0:
        print(n)
    elif n % 2 == 0:
        print(n+1)
    else:
        print((n+1)//2)


pizzaCuts(n)
