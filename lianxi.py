"""
装饰函数（时间）
"""


import time


def get_time(f):
    def wrapper(*args,**kwargs):
        begin_time=time.time()
        res=f(*args,**kwargs)
        end_time=time.time()
        print(end_time-begin_time)
        return res
    return wrapper
@get_time
def fun():
    s=0
    for i in range(1,100000001):
        s+=i
    return s
fun()