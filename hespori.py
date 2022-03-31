import random

class Hespori:
    def __init__(self):
        self.hp = 300
        self.ticks = 0
        self.nextticks = 0

    def __bool__(self):
        return self.hp >= 0

    def attack(self, acc, maxh, ticks):
        self.ticks += self.nextticks
        self.nextticks = ticks
        if random.random() <= acc:
            self.hp -= random.randint(0, maxh)

    def dds(self):
        acc = 0.8011
        maxh = 44
        self.attack(acc, maxh, 4)
        self.attack(acc, maxh, 4)

    def tentwhip(self):
        acc = 0.8263
        maxh = 50
        self.attack(acc, maxh, 4)

    def claws(self):
        acc = 0.9981
        maxh = 40
        self.attack(acc, maxh, 0)
        self.attack(acc, maxh/2, 1)
        self.attack(acc, maxh/4, 0)
        self.attack(acc, maxh/4, 3)

    def chally(self):
        acc = 0.8217
        maxh = 62
        self.attack(acc, maxh, 0)
        self.attack(0.7623, maxh, 7)

    def whack(self):
        acc = 0.8391
        maxh = 60
        self.attack(acc, maxh, 6)

N = 10000
cnt = 0
for i in range(N):
    h = Hespori()
    h.dds()
    h.dds()
    h.tentwhip()
    h.whack()
    h.tentwhip()
    h.tentwhip()
    h.chally()
    if h.hp <= 0:
        cnt += 1
print(f'Took {h.ticks} ticks')
print(f'1 / {N / cnt}')
