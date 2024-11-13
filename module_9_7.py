def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(1, result+1):
            if result % i == 0:
                k +=1
        if k == 2:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    summ = a + b + c
    return summ

result = sum_three(2, 3, 6)
print(result)