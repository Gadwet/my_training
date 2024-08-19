first = 25
second = 10
third = 5
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second or not second == third or not first == third:
    print(0)