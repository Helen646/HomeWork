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
            raise ValueErrore
    def current(self):
        return (self.x,self.y)
