smile = '\U0001f600'
for num in range(10):
    count = 0
    smile_string = ''
    while count <= num:
        smile_string += '\U0001f600'
        count += 1
    print(smile_string)
for number in range(1, 11):
    print('\U0001f600' * number)
some_list = [[0, 12], [33, 'Hello'], [True, 0]]
for inner_list in some_list:
    for element in inner_list:
        print(element)
