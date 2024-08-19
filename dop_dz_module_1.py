grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
s1 = sum(grades[0]) / len(grades[0]) # sum - Суммирование чисел, len - Колличество символов.
s2 = sum(grades[1]) / len(grades[1])
s3 = sum(grades[2]) / len(grades[2])
s4 = sum(grades[3]) / len(grades[3])
s5 = sum(grades[4]) / len(grades[4])
# print(s1, s2, s3, s4, s5)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
spisok = list(students) # Преобразование в список.
sorted_s = sorted(spisok) # Сортировка списка.
# print(sorted_s)
n1 = sorted_s[0]
n2 = sorted_s[1]
n3 = sorted_s[2]
n4 = sorted_s[3]
n5 = sorted_s[4]
para = {n1:s1, n2:s2, n3:s3, n4:s4, n5:s5}
print(para)