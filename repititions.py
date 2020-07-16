def repitition():
    s = str(input())
    maximum = 0
    count = 0
    current = ""

    for c in s:
        if c == current:
            count += 1
        else:
            count = 1
            current = c
        maximum = max(count, maximum)
    return maximum


print(repitition())
