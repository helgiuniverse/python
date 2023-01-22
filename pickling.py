import pickle
macbook = (
    'gray',
    'Apple',
    'MacBook Pro',
    (
        ('Memory', 16),
        ('Year', 2017),
        ('MacOS', 13)
    )
)

with open('macbook.pickle', 'bw') as macbook_file:
    pickle.dump(macbook, macbook_file)
with open('macbook.pickle', 'br') as macbook_retrieved:
    macbook_from_file = pickle.load(macbook_retrieved)
print(macbook_from_file)
color, mark, model, characteristics = macbook_from_file
print(color, mark, model, characteristics)
for x in characteristics:
    characteristic, value = x
    print(characteristic + ' of macbook is ' + str(value))
