class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y
    
    def reflect_x(self):
        self.y = -1*self.y
        return "({0}, {1})".format(self.x, self.y)
