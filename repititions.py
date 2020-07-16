def repitition():
    sequence = str(input())
    maximum = 0
    count = 0
    current = ""

    for char in sequence:
        if char == current:
            count += 1
        else:
            count = 1
            current = char
        maximum = max(count, maximum)
    return maximum


print(repitition())
