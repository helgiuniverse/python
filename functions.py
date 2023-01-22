# def cat_voice():
#     print('Meow!')
#
#
# def dog_voice():
#     print('Woof!')
# dog_voice()
# cat_voice()

def cat_voice():
    return 'Meow!'


def dog_voice():
    return 'Woof!'


x = dog_voice()
y = cat_voice()
print(x * 2, y * 2)


def get_voice(voice):
    return voice + '!'


hi = get_voice('hi')
print(hi)


def get_odd_numbers_1(a, b):
    some_list = [num for num in range(a, b+1) if num % 2 == 1]
    return some_list


def get_odd_numbers_2(a, b):
    some_list = []
    for num in range(a, b+1):
        some_list.append(num)
    return some_list
