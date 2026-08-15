import random


def func_poor_network():
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Connection established"
