# @Time : 2020/2/16 10:56
# @Author : tongyue


class A:
    def __enter__(self):
        a = 1
        return a
    def __exit__(self, exc_type, exc_val, exc_tb):
        b = 1

with A() as a_obj:
    print(a_obj)

'''
as 后面的对象并不是上下文， 而是__enter__的返回值
'''
