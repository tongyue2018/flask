# @Time : 2020/2/19 17:43
# @Author : tongyue
import threading,time

'''
1.更加充分的利用cpu性能优势
2.单核cpu只能同时跑1个线程
3.python没办法利用多核CPU的优势
4.python多线程是个鸡肋（不对）--
5.GIL 全局解释器锁  
6.锁 目的是做到线程安全
7.内存资源 1个进程 被多个线程共享
8.线程不安全 

'''
#主线程
t = threading.current_thread()
threadName = t.getName()
print(threadName)
print(time.asctime())


def worke1():
    time.sleep(2)
    t = threading.current_thread()
    threadNameWork = t.getName()
    str = "我是一个worker子线程:{}".format(threadNameWork)
    print(str)
    print(time.asctime())

def worker2():
    time.sleep(2)
    t = threading.current_thread()
    threadNameWork = t.getName()
    str = "我是一个worker子线程:{}".format(threadNameWork)
    print(str)
    print(time.asctime())
#子线程
tr1 = threading.Thread(target=worke1)
tr2 = threading.Thread(target=worker2,name="我的第二个子线程")


tr1.start()
tr2.start()
