def all_variants(text):
    len_str = len(text) # создаём переменную которая принимает длину атрибута функции
    for start in range(len_str): # создам цикл for который будет началом перебора атрибута функции
        for end in range(start + 1, len_str + 1): # создам цикл for который будет концом перебора атрибута функции
            yield text[start:end] # оператор который возвращает переданные значения в text

# Код для проверки:
a = all_variants("abc")
for i in a:
    print(i)