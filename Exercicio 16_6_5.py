import math

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def collision(r1,r2):
    range_x1 = r1.corner.x + r1.width
    range_y1 = r1.corner.y + r1.height
    range_x2 = r2.corner.x + r2.width
    range_y2 = r2.corner.y + r2.height

    possi_x =  False
    possi_y = False
    if not ((r1.corner.x >range_x2) or (range_x1<r2.corner.x)):
        possi_x =  True
    if not ((r1.corner.y < range_y2) or (range_y1<r2.corner.y)):
        possi_y =  True

    return possi_x and possi_y