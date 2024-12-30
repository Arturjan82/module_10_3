# -- coding: utf8 --
import threading
import random
import time

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(100):
            rand_number = random.randint(50, 100)
            self.lock.acquire()
            if self.balance < 500 and self.lock.locked():
                self.balance += rand_number
                print(f'Пополнение: {rand_number}. Баланс: {self.balance}')

            self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand_number = random.randint(50, 100)
            print(f'Запрос на {rand_number}')
            self.lock.acquire()
            if rand_number <= self.balance:
                self.balance -= rand_number
                print(f'Снятие: {rand_number}. Баланс: {self.balance}')

            else:
                print('Запрос отклонён, недостаточно средств')
            self.lock.release()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')