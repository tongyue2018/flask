# @Time : 2020/2/20 15:11
# @Author : tongyue
from werkzeug.local import LocalStack

s = LocalStack()

s.push(1)
s.push(2)
print(s.top) #取栈顶元素而已, top没有()是加了@property
print(s.pop())#弹出栈顶元素
print(s.top) #取栈顶元素而已


