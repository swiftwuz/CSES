# Weird Algorithm


def weird():
    integer = int(input())
    while integer != 1:
        print(integer, '', end='')
        if integer % 2 == 0:
            integer = (integer//2)
        elif integer % 2 == 1:
            integer = (integer * 3) + 1
    return integer


print(weird())
