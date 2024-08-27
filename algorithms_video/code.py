num = int(input())


def is_power(num: int):
    s = ""
    while num != 0:
        bt += num & 1
        num = num >> 1
    return bt == 1


print(is_power(num))
