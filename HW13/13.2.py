class Point
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move (self,destanse,direction):
        if direction =="left":
            self.x= -destanse
        elif direction =="right":
            self.x= +destanse
        elif direction =="up":
            self.y= +destanse
        elif direction =="down":
            self.y= -destanse
        else:
            raise ValueError
    def current(self):
        return (self.x,self.y)
class Rectangle:
    def rectanglee(self,x,y,w,h):
        left_down=Point(x,y)
        left_up = Point(x,y +h)
        right_up = Point(x+w,y+h)
        right_down = Point(x+w, y)
        self.move_list=[left_down,left_up,right_up,right_down]
        self.w=w
        self.h=h
    def move(self,distanse,direction):
        for i in self.move_list:
            i.move(distanse,direction)
    def move_list(self):
        for i in self.move_list:
            return ((self.left_down), (self.left_up), (self.right_up), (self.left_down))
