# Missing Number

try:
    def missing_number():
        num = int(input())
        result = num*(num+1)//2 - sum(map(int, input().split()))
        return result

    print(missing_number())

except EOFError as e:
    print(end="")
