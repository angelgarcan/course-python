from collections import namedtuple
from datetime import datetime
import enum
import multiprocessing as mp
import random
import time


class C(enum.Enum):
    Green = "\u001b[32m"
    Magenta = "\u001b[35m"
    Yellow = "\u001b[33m"
    Cyan = "\u001b[36m"
    Blue = "\u001b[34m"
    Red = "\u001b[31m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"
    # Black = "\u001b[30m"


Chopstick = namedtuple('Chopstick', ['s', 'name'])


class Philosopher():

    def __init__(self, name, color: C, right_chopstick: Chopstick, left_chopstick: Chopstick):
        self.name = name
        self.color = color
        self.right_chopstick = right_chopstick
        self.left_chopstick = left_chopstick
        self.eating_time = random.randint(2, 5)
        self.thinking_time = random.randint(2, 5)
        self.p = mp.Process(target=self.run)

    def think(self):
        self.log(f"START Thinking for {self.thinking_time} seconds")
        time.sleep(self.thinking_time)
        self.log("END   Thinking")

    def _acquire_chopsticks(self) -> bool:
        self.log(
            f"Trying to acquire {self.right_chopstick.name} and {self.left_chopstick.name} chopsticks")

        if self.right_chopstick.s.acquire():  # Waiting for right chopstick.
            self.log(f"Acquired {self.right_chopstick.name} chopstick")
            # Getting the left chopstick or release the right one.
            if self.left_chopstick.s.acquire(block=False):
                self.log(f"Acquired {self.left_chopstick.name} chopstick")
                self.log("BOTH chopsticks acquired")
                return True
            else:
                self.log(
                    f"{self.left_chopstick.name} chopstick cannot be acquired. Releasing {self.right_chopstick.name}")
                self.right_chopstick.s.release()
                self.log(f"{self.right_chopstick.name} chopstick released")
        self.log("NONE chopsticks acquired")
        return False

    def _release_chopsticks(self):
        self.log("Releasing chopsticks")
        # Release both chopsticks.
        self.right_chopstick.s.release()
        self.left_chopstick.s.release()
        self.log("Released chopsticks")

    def eat(self):
        while not self._acquire_chopsticks():
            self.waiting()

        self.log(f"START Eating for {self.eating_time} seconds")
        time.sleep(self.eating_time)
        self.log("END   Eating")

        self._release_chopsticks()

    def waiting(self):
        self.log("START Waiting")
        time.sleep(1)  # Everyone waits the same.
        self.log("END   Waiting")

    def run(self):
        while True:
            self.think()
            self.eat()

    def log(self, msg):
        print(f"{self.color.value}{datetime.utcnow().isoformat(sep=' ', timespec='microseconds')}|{self.name}|{msg}{C.Reset.value}")


if __name__ == '__main__':
    print("START OF PROGRAM")

    n = 3
    chopsticks = [Chopstick(mp.BoundedSemaphore(), f"CH{i}") for i in range(n)]

    phils = []
    for i in range(n):
        phil = Philosopher(f"P{i}", list(C)[i],
                           right_chopstick=chopsticks[i],
                           left_chopstick=chopsticks[(i+1) % n])
        phils.append(phil)
        phil.p.start()

    for phil in phils:
        phil.p.join()

    # c1 = Chopstick(mp.BoundedSemaphore(), "CH1")
    # c2 = Chopstick(mp.BoundedSemaphore(), "CH2")
    # c3 = Chopstick(mp.BoundedSemaphore(), "CH3")

    # phil1 = Philosopher("P1", C.Green, right_chopstick=c1, left_chopstick=c2)
    # phil1.p.start()

    # phil2 = Philosopher("P2", C.Magenta, right_chopstick=c2, left_chopstick=c3)
    # phil2.p.start()

    # phil3 = Philosopher("P3", C.Yellow, right_chopstick=c3, left_chopstick=c1)
    # phil3.p.start()

    # phil1.p.join()
    # phil2.p.join()
    # phil3.p.join()

    print("END OF PROGRAM")
