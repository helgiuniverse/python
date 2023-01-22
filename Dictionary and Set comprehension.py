some_dict = {'first': 1, 'second': 2, 'third': 4}
new_dict = {key: value ** 2 for key, value in some_dict.items()}
print(some_dict)
print(new_dict)
some_list = [num for num in range(2, 10)]
print(some_list)
new_dict_from_list = {num: num ** 2 for num in some_list}
print(new_dict_from_list)
# x = input('Enter some numbers')
# numbers = [int(num) for num in x]
# new_dict_from_numbers = {num: num ** 2 for num in numbers}
# print(new_dict_from_numbers)
number_list = [-12, 2, 0, 123, -5, -432, 13]
number_dict = {num: 'positive' if num > 0 else 'negative' if num < 0 else 'zero' for num in number_list}
print(number_dict)
new_set_from_list = {num ** 2 for num in some_list}
print(new_set_from_list)
