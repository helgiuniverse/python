from random import shuffle
from random import randint
# range(first number, last index number, step)
for x in range(1, 21, 3):
    print(x)
print(list(range(5)))
for index, item in enumerate('ABCDEFG'):
    print(index, item)
print('Python' in 'Hello Python!')
print(min(1, 2, 4), max(23, 4, 123))
some_list = [12, 123, '23', 123.312, 0]
print(some_list)
shuffle(some_list)
print(some_list)
print(randint(12, 123))
