greeting = 'Hello'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)
letter_list = [letter for letter in 'Hello']
print(letter_list)
number_list = [int(num) for num in '0123456789']
print(number_list)
number_list_2 = [int(num)**2 for num in '0123456789']
print(number_list_2)
new_list = [num for num in range(1, 20) if num % 4 == 0]
print(new_list)
some_list = [-1, 2, 123, -12, 125, 3, 0, -5]
new_list_2 = ['+' if num > 0 else '-' for num in some_list]
print(new_list_2)

greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings_list = [greeting[1] for greeting in greetings]
print(new_greetings_list)

new_greetings_list_2 = []
for greeting in greetings:
    new_greetings_list_2.append(greeting[1])
print(new_greetings_list_2)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_digits_1 = [digit for digit in digits if digit % 2 == 0]
print(odd_digits_1)
odd_digits_2 = []
for digit in digits:
    if digit % 2 == 0:
        odd_digits_2.append(digit)
print(odd_digits_2)