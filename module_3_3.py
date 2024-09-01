def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print(a, b,)
    print(a)
    print()

values_list = ['Coffee', 255, False]
values_dict = {'a': 'Orange', 'b': 194, 'c': 25.5}

values_list_2 = ['Tea', 1473]

# 1.Функция с параметрами по умолчанию:
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
print_params(*values_list_2, 42)