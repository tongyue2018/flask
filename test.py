# @Time : 2020/3/28 9:59 
# @Author : tongyue \\


class Animal(object):
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, float):
            raise ValueError("高度应该是小数")
        if value < 0 or value > 300:
            raise ValueError("高度范围是0到300cm")
        self._height = value

d = Animal()
d.height = -1
print(d.height)