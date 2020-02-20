# @Time : 2020/2/20 15:46
# @Author : tongyue
import threading

from werkzeug.local import LocalStack

myStack = LocalStack()
myStack.push(1)
print("主线程myStack.top:{}".format(myStack.top))

def workerA():
    myStack.push(2)
    print("线程1 myStack.top:{}".format(myStack.top))

def workerB():
    myStack.push(3)
    print("线程2 myStack.top:{}".format(myStack.top))

#子线程
trA = threading.Thread(target=workerA)
trB = threading.Thread(target=workerB)
trA.start()
trB.start()

'''
myStack同一个对象各个线程的栈互不干扰

'''
