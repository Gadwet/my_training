import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            balance_replenishment = randint(50, 500)
            with self.lock:
                if self.balance < 500 and self.lock.locked():
                    self.balance += balance_replenishment
                    print(f'Пополнение: {balance_replenishment}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            balance_removal = randint(50, 500)
            print(f'Запрос на {balance_removal}.')
            with self.lock:
                if balance_removal <= self.balance:
                    self.balance -= balance_removal
                    print(f'Снятие: {balance_removal}. Баланс: {self.balance}.')
                else:
                    print(f'Запрос отклонён, недостаточно средств.')
            time.sleep(0.001)

# Код для проверки:
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}.')