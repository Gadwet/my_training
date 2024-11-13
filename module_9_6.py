def all_variants(text):
    for i in range(len(text)): # создаём цикл for в котром i будет принимать перебор длины text
        for j in range(len(text) - i): # создаём цикл for в котром j будет принимать перебор длины text вычитаемой из него переменную i
            yield text[j:j + i + 1] # оператор yield который будет возвращать диапазон атрибута функции

# Код для проверки:
a = all_variants("abc")
for i in a:
    print(i)