#__author: Liu Zheng
#date:2018/6/21


class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

s = Screen()
s.width = 10
s.height = 10
print(s.resolution)

