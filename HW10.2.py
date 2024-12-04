import threading
import time

class Knight(threading.Thread):
    day = 0
    enemy = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy:
            self.day += 1
            self.enemy -= self.power
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemy} воинов.')
            time.sleep(1)
        if self.enemy == 0:
            print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()