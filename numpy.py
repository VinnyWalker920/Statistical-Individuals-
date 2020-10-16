import random


def randint(maxvalue, size=1):
    l = []
    for i in range(size):
        l.append(random.randint(1, maxvalue))
    return l
