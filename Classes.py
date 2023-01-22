class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_1 = BlogPost(user_name='Alex', text='bla', number_of_likes=19)
post_2 = BlogPost(user_name='John', text='bla-bla', number_of_likes=15)
post_1.number_of_likes = 12000
print(post_1.number_of_likes, post_2.number_of_likes)


class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, sum_of_money):
        self.balance += sum_of_money

    def withdraw(self, sum_of_money):
        self.balance -= sum_of_money


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f'Hi, my name is {self.name}')


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print(f'Hi, my name is {self.name} and I will kill you')

    def kill(self, game_character):
        game_character.health = 0
        self.level += 1
        print('Bang-bang, now you\'re dead')


class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return f'Chain with {self.number_of_items} items'

    def __len__(self):
        return self.number_of_items


class PersonalComputer:
    format_of_pc = 'Notebook'
    is_on = False
    active_computers = 0

    @classmethod
    def add_new_computer_from_string(cls, data_string):
        mark, model, color = data_string.split(',')
        new_computer = cls(mark, model, color)
        return new_computer

    @classmethod
    def get_active_computers(cls):
        print(PersonalComputer.active_computers)

    def __init__(self, mark, model, color):
        self.mark = mark
        self.model = model
        self.color = color

    def computer_power_on(self):
        self.is_on = True
        print('{mark} {model} is on'.format(mark=self.mark, model=self.model))
        PersonalComputer.active_computers += 1

    def open_app(self, app, dic):
        print('{app} from {dic} is open on {model}'.format(model=self.model, app=app, dic=dic))

    def change_color(self, new_color):
        self.color = new_color


class GamersComputer(PersonalComputer):
    type_of_computer = 'Gamer\'s computer'
    format_of_pc = 'Gamer\'s notebook'

    def __init__(self, mark, model, color):
        PersonalComputer.__init__(self, mark, model, color)

    def open_app(self, app, dic):
        print('{app} from {dic} is open on gamer\'s notebook {mark} {model}'.
              format(model=self.model, app=app, dic=dic, mark=self.mark))


my_computer = PersonalComputer(mark='Apple', model='MacBook Pro', color='Space Gray')
print(my_computer.color + ', ' + my_computer.model + ', ' + my_computer.mark + ', ' + my_computer.format_of_pc)
format_of_something_pc = PersonalComputer.format_of_pc
print(format_of_something_pc)
print(my_computer.is_on)
my_computer.computer_power_on()
print(my_computer.is_on)
my_computer.open_app('Safari', '/user/oleg/programs')
my_computer.change_color('Gold')
print(my_computer.color)
some_computer = PersonalComputer(mark='Asus', model='ZenBook X', color='Black')
print(PersonalComputer.active_computers)
some_computer.computer_power_on()
PersonalComputer.get_active_computers()
new_computer_lenovo = PersonalComputer.add_new_computer_from_string('Lenovo, IdeaPad 3, White')
print(new_computer_lenovo.mark, new_computer_lenovo.model, new_computer_lenovo. color)
new_computer_lenovo.computer_power_on()
PersonalComputer.get_active_computers()
gamer_computer = GamersComputer(mark='Asus', model='Zephyrus', color='Red')
print(gamer_computer.type_of_computer)
gamer_computer.computer_power_on()
PersonalComputer.get_active_computers()
gamer_computer.open_app('Half_life', '/user/oleg/Desktop')


class Walkable:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'Hello, my name is {self.name} and i can walk')


class Flyable:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'Hello, my name is {self.name} and i can fly')


class Swimmable:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'Hello, my name is {self.name} and i can Swim')


class Duck(Walkable, Flyable, Swimmable):
    def __init__(self, name):
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)
        Swimmable.__init__(self, name)

    def __str__(self):
        return f'My name is {self.name} i am duck'

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print(f'Duck {self.name} is killed')


donald = Duck('Donald')
print(len(donald))
print(donald)
del donald
