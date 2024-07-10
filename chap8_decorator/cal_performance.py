from time import time

def performance(func):
    
    def wrapper(*args, **kwargs):
        tStart = time()
        func(*args, **kwargs)
        tEnd = time()
        print(f"func takes {tEnd-tStart} s")

    return wrapper
    
@performance
def myFunc():
    # 做一個單純消耗時間的運算
    for i in range(10000):
        d = i**2

myFunc()
