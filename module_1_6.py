# Работа со словарями:
my_dict = {'Vladimir' : 1930 , 'Nikolay' : 1940 , 'Oksana' : 1950}
print(my_dict)
print(my_dict['Nikolay'])
my_dict['Larisa'] = 1960
print(my_dict)
my_dict.update({'Vasiliy' : 1970,
                'Ivan' : 1980  })
a = my_dict.pop('Nikolay')
print(a)
print(my_dict)

# Работа с множествами:
my_set = {20, 21, 22, 23, 20, 21, 22, 'Hello', 'World', 'Data', 'World', 'Data'}
print(my_set)
my_set.update({'Life',
               'Driver'})
my_set.discard('Hello')
print(my_set)