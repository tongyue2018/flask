import sys
# sys.path.append('E:\\pythonProject\\python_study\\python初学\\初学(2)')
sys.path.append('../') #效果和上面绝对路径一致

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from borax.calendars.lunardate import LunarDate
from  ServerJiangNotify import ServerJiangNoify

class NotifyBirthday:
    def __init__(self,**birthdayDict):
        self.__birthdayDict = birthdayDict
    def getBirthdayDict(self):
        return self.__birthdayDict
    def notifyBirthday(self): # 距离生日7 、3 、1 、0天时通知
        flag = False #标记今天没有人过生日
        for name,birthday in self.__birthdayDict.items():
            ##获取今天的农历日期
            todayNongli = LunarDate.today()
            birthday = LunarDate(todayNongli.year,birthday.month,birthday.day,0)#将生日的年份改成今年，方便计算还有多少天过生日，直接与当前农历日志相减
            howMuchDays = birthday.offset - todayNongli.offset
            if(howMuchDays == 7 or howMuchDays == 3 or howMuchDays == 1 or howMuchDays == 0):
                text = '{name}的生日还有{howMuchDays}天，要祝福呦~。'.format(name=name,howMuchDays=howMuchDays)
                desp = '###{name},祝你生日快乐,健健康康~~'.format(name=name) # 内容支持markdown
                serverJiangNoify = ServerJiangNoify(text,desp)  #初始化.
                print(serverJiangNoify.sendMessage())
                flag = True #无人过生日
        text = "加油工作,加油学习~"+str(time.time())
        desp = "###没钱不行，没钱不行，没钱不行~"
        serverJiangNoify = ServerJiangNoify(text, desp)
        print(serverJiangNoify.sendMessage())

sched = BlockingScheduler()
@sched.scheduled_job('cron', hour = 8,minute = 59)
def notifyBirthday():
    print(time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ())))
    birthdayDict = {
        "我": LunarDate(1986, 10, 3, 0),
        "婷婷": LunarDate(1987, 4, 2, 0),
        "东北爸": LunarDate(1967, 5, 28, 0),
        "东北妈": LunarDate(1965, 11, 27, 0),
        "湖南爸": LunarDate(1953, 9, 25, 0),
        "湖南妈": LunarDate(1957, 5, 29, 0),
    }
    notifyBirthday = NotifyBirthday(**birthdayDict)
    notifyBirthday.notifyBirthday()

if __name__ == '__main__':
    sched.start()
