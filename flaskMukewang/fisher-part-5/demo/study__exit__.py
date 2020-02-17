# @Time : 2020/2/16 10:56
# @Author : tongyue


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print("process exception")
            print(exc_val)
        else:
            print("no exception")

        print('close resource')

        return True  # 默认会False 抛出异常到外面，选择True则不会向外部抛出异常 而是在__exit__内部处理

    def query(self):
        print('query data')


with MyResource() as myresouce:
    1 / 0
    myresouce.query()

'''
as 后面的对象并不是上下文， 而是__enter__的返回值
def __exit__(self, exc_type, exc_val, exc_tb) 后面三个参数是处理异常用的

'''
