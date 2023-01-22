# x = 0
#
#
# def print_x():
#     x = 1
#     def print_nonlocal_and_global_x():
#         global x
#         print(x)
#     print_nonlocal_and_global_x()
#     print(x)
# print_x()


def print_x():
    x = 1

    def print_nonlocal_and_global_x():
        nonlocal x
        print(x)

    print_nonlocal_and_global_x()


print_x()
