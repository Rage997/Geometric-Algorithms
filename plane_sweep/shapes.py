import math
import sympy.geometry
import numpy as np

class Rectangle:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

class Circle:
    def __init__(self, x, y, r):    
        self.x = x
        self.y = y
        self.r = r
    
    def intersection(self, disk):
        '''
        Intersection between two circles. There are 3 possible cases:
        1) No intersection
        2) Unique intersection (tangency)
        3) Double intersection
        '''
        # d1 = self
        # d2 = disk
        # diam = math.sqrt( (d2.x - d1.x)**2 + (d2.y - d1.y)**2)

        # # 1) No intersection
        # if diam > (d1.r + d2.r):
        #     return []
        # if diam == 0 and d1.r == d2.r:
        #     return []
        # else:
        #     #ref: https://gist.github.com/xaedes/974535e71009fa8f090e
        #     a = ( d1.r**2 - d2.r**2)/(2*diam)
        #     h = math.sqrt(disk.r**2 - a**2)

        # Using sympy cause I'm lazy
        p1 = sympy.geometry.Point(self.x, self.y)
        p2 = sympy.geometry.Point(disk.x, disk.y)
        c1 = sympy.geometry.Circle(p1, self.r)
        c2 = sympy.geometry.Circle(p2, disk.r)

        intersection = c1.intersection(c2)
        if len(intersection) == 0:
            # 1) no intersection
            return []
        elif len(intersection) == 1: 
            # 2() tangency
            p = intersection[0]
            x, y= p.x, p.y
            return [x, y]
            intersection.append(intersection[0])
        elif len(intersection) == 1:
            p1 = intersection[0]
            p2 = intersection[1]
            x1,y1 = p1.x, p1.y
            x2,y2 = p2.x, p2.y
            return [x1, y1, x2, y2]