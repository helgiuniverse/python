person = {
    'name': 'Jack',
    'age': 18,
    'job': 'teacher',
    'hobbies': ['football', 'guitar', 'python'],
    'cars': {
        'mazda': 'cx5',
        'toyota': 'corolla',
        'tesla': 'model x'
    }
}
print(person)
print(person['job'])
person['surname'] = 'Jefferson'
new_person = {
    'name': 'Alex',
    'surname': 'Wild'
}
print(new_person)
new_person.clear()
print(new_person)
del new_person
print(person['hobbies'][0])
print(person['cars']['mazda'])
print(person.keys())
print(person.values())
print(person.items())
