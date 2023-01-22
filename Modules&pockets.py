from random import shuffle as sf
import math
import utils
import termcolor
x = [1, 2, 2, 3, 12]
sf(x)
print(x)

print(math.sqrt(123456789))
print(math.factorial(987))
print(math.pow(876, 54), 876 ** 54)
utils.hello_world()
utils.greeting_with_name('Jack')
color = utils.get_favorite_color()
number = utils.get_favorite_number()
print(color, number)
print(termcolor.colored('LOL', 'green'))
if __name__ == '__main__':
    sf(x)
