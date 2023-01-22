print(1+1)
print('1'+'1')
name = 'Jack'
age = 21

name_and_age = 'My name is {0}, i`m {1} y.o'.format(name, age)
print(name_and_age)

print('My name is {}'.format(name))

weekdays = "There is a seven day a week:  {sun}, {mo}, {th}".format(sun="Sunday", mo="Monday", th="Thursday")

print(weekdays)

print(f'My name is {name}')

print("%s is %d y.o" % (name, age))

print("""

{0:15.4f}{1:15.4f}{2:15.4f}{3:15.4f}

{4:15.4f}{5:15.4f}{6:15.4f}{7:15.4f}

""".format(15.12312, 3.1231231, 678879.123123, 12312.213123, 546.54645, 45666.45645, 324.2342342, 0.456456))
