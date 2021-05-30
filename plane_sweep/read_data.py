import numpy as np
from shapes import Rectangle, Circle

def read_data(filename):
    '''Reads data as described in pdf'''
    with open(filename) as f:
        idx = 0
        rect = None
        disk = []
        for line in f:
            line = line.rstrip() # remove endline char
            line  = line.split(' ') # split by coma
            if idx == 0:
                x_min, x_max = int(line[0]), int(line[1])
                
            elif idx == 1:
                y_min, y_max = int(line[0]), int(line[1])
            else:
                x, y, r = int(line[0]), int(line[1]), int(line[2])
                disk.append(Circle(x, y, r))
            idx += 1

        rect = Rectangle(x_min, x_max, y_min, y_max)
        return rect, disk