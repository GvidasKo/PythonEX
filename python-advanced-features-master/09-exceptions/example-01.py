import random

random_exp = [IndexError, SyntaxError, KeyboardInterrupt]


def random_exeption():
    print(random.choice(random_exp))

