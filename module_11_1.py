######### Работа c библиотекой Requests
import requests

#1
request1 = requests.get('https://music.yandex.ru/chart') # Запрашиваем информацию с сайта
print(f'Первый запрос:\n{request1.text}\n') # Получаем и выводим информацию с сайта
#2
request2 = requests.get('https://www.dns-shop.ru/about')
print(f'Второй запрос:\n{request2.text}\n')
#3
request3 = requests.get('https://yandex.ru/pogoda/213')
print(f'Третий запрос:\n{request3.text}\n')


######### Работа c библиотекой Pandas
import pandas as pd

#1
series_example = pd.Series([4, 7, -5, 3])
print(f'{series_example}\n')

#2
city = {'Город': ['Москва', 'Новосибирск', 'Санкт-Петербург', 'Екатеринбург'],
        'Год основания': [1147, 1893, 1703, 1723],
        'Население': [13.1, 1.6, 5.5, 1.5]}

df = pd.DataFrame(city)
sort = df.sort_values('Год основания', ascending=True)
print(f'{sort}\n')

#3
data_import = pd.read_csv('Cars.csv') # Импорт данных
sort = data_import.sort_values('Тип двигателя', ascending=True).tail() # Анализируем и фильтруем данные
print(sort) # Выводим данные


######### Работа c библиотекой Matplotlib
import matplotlib.pyplot as plt

#1
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [25, 32, 36, 40, 45, 43, 38, 32, 36, 39, 43, 47, 53, 41, 39, 47, 50, 62, 67, 70]

plt.plot(x, y, marker='o', markersize=7)
plt.xlabel('День') #Подпись для оси х
plt.ylabel('Цена') #Подпись для оси y
plt.title('Курс валюты') #Название
plt.show()

#2
x = ['Апрель', 'Май', 'Июнь', 'Июль', 'Август']
y = [5573, 2564, 3882, 4123, 5031]
plt.bar(x, y, label='Величина произведённых изделий')
plt.xlabel('Месяц года')
plt.ylabel('Количество изделий')
plt.title('Статистика')
plt.legend()
plt.show()

#3
month = ['Апрель', 'Май', 'Июнь', 'Июль', 'Август']
defective_products = [434, 247, 352, 340, 495]

plt.pie(defective_products, labels=month, autopct='%1.1f%%')
plt.title("Колличество бракованных изделий")
plt.show()