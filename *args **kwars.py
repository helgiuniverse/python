def sum_num(*args):
    count = 0
    for num in args:
        count += num
    return count


print(sum_num(1, 2, 14, 14))

def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello, {}'.format(kwargs['name']))
    else:
        print('Please, enter your name')


hello_with_kwargs(gender='male', name='John', surname='Watson')


def greeting(hi, *args):
    print(hi+' {} {}, you are in system! '.format(args[0], args[1]))


greeting('Hello', 'Garry', 'Potter')


def worker_data(name_of_list, **kwargs):
    print(name_of_list)
    print('''name is {},
hobby is {},
id : {}'''.format(kwargs['name'], kwargs['hobby'], kwargs['id']))


worker_data('Alex`s data', name='Alex', hobby='guitar', id='98144')


def is_cat_here(*args):
    for element in args:
        if element.lower() == 'cat':
            return True
        else:
            return False


x = is_cat_here('dog', 'smth', 1, 123, True)
print(x)


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False


y = is_item_here('cat', 'fog', 'sheesh', 'sus', 'cat')
print(y)


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))


your_favorite_color('blue')
