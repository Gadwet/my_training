def introspection_info(obj):
    obj_type = type(obj).__name__ # Определение типа объекта

    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
    else:
        attributes.append(attr)

    module = obj.__class__.__module__ # Определение модуля, к которому объект принадлежит

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module} # Создание словаря с информацией об объекте

    return info

# Код для проверки:

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Hello')
print(string_info)

# Интроспекция списка
list_info = introspection_info([10, 45, 1.0, 'word'])
print(list_info)
