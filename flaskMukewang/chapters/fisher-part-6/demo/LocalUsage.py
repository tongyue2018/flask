# @Time : 2020/2/19 17:43
# @Author : tongyue
import threading,time
from werkzeug.local import Local


#主线程
t = threading.current_thread()
threadName = t.getName()
print(threadName)
print(time.asctime())

'''

线程隔离对象--Local，属于werkzeug库，并不属于flask
Local是对字典进行操作，做到线程隔离，比如dict{'当前线程号a':对象a，'当前线程号b':对象b}
LocalStack是对Local进行封装 实现线程隔离的栈结构

werkzeug--> LocalStack--> Local--> dict

'''
class MainClass:
    b = 1

myObj = Local()

def workerA():
    myObj.b = 2
    print('子线程myObj.b:{}'.format(myObj.b))

def workerB():
    myObj.b = 3
    print('子线程myObj.b:{}'.format(myObj.b))


#子线程
trA = threading.Thread(target=workerA)
trB = threading.Thread(target=workerB)
trA.start()
trB.start()


