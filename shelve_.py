import shelve
with shelve.open('companies') as companies:
    companies['apple'] = 'USA'
    companies['xiaomi'] = 'China'
    companies['samsung'] = 'Korea'
    companies['lg'] = 'Japan'

    print(companies['xiaomi'])
    for key in companies:
        print(key)
    # del companies['apple']
    # for key in companies:
    #   print(key)
    while True:
        key = input('Enter company name: ')
        if key == 'quit':
            break
        if key in companies:
            print(companies[key])
        else:
            print('We don\'t have a ' + key)

    ordered_list_of_companies = list(companies.keys())
    ordered_list_of_companies.sort()
    print(ordered_list_of_companies)