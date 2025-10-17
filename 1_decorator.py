# 1_decorator.py : demonstration of decorator

import time
from typing import Any,Callable



def timer(f:Callable[...,Any]) -> Callable[...,Any]:
    '''decorator measure time elapsed during function'''
    def g(*args,**kwargs):
        t = time.perf_counter()
        _ = f(*args,**kwargs)
        print(f'{f.__name__} executed in {time.perf_counter()-t:6f} seconds')
        return _
    return g

@timer
def f(n:int=10):
    '''return nxn timetable'''
    return [[i*j for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    f(1000)