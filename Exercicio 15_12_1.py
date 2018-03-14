import math

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

def distance(p,q):
    return math.sqrt( (p.x-q.x)**2 + (p.y-q.y)**2 )
