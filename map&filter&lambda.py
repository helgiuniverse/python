some_list = list(range(10))

# def cube(num):
#     return num ** 3
# lambda num: num**3


def cube(num):
    return num ** 3


some_list_cube = list(map(cube, some_list))
print(some_list_cube)


def is_odd(num):
    if num % 2 == 0:
        return True
    elif num % 2 == 1:
        return False
    elif num <= 0:
        return None


odd_list = list(filter(is_odd, some_list))
print(odd_list)
print(list(map(lambda num: num*2, some_list)))
