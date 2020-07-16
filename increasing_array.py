def increasing_array():
    arr_size = int(input())
    arr_contents = list(map(int, input().split()))

    turns = 0
    temp = arr_contents[0]
    for i in range(1, arr_size):
        if arr_contents[i] < temp:
            turns += temp - arr_contents[i]
        else:
            temp = arr_contents[i]
    return turns


print(increasing_array())
