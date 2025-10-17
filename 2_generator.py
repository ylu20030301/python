# 2_generator.py : demonstration of generator

from typing import Generator

def fibonacci(n:int=10) -> Generator:
    '''
    yield first \<int n> fibonacci numbers

    i:
        n (int): len

    o:
        r (list[int]): list of fibonacci numbers
    '''
    if n <= 0: return
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(fibonacci(10)))