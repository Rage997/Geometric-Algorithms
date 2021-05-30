from read_data import read_data
from binary_tree import binaryTree
from event import PriorityQueue, Event

# Read the data
rect, disk = read_data('./input.txt')
# Sort the disks in ascending order by x coordinate
# disk.sort(key=lambda c: c.x, reverse=False)

events = [] # event queu

for d in disk:
    # Generate two events for both leftmost and rightmost point of each disk
    e1 = Event()
    e1.val = d.x - d.r
    e1.disk = d
    e2 = Event()
    e2.val = d.x + d.r
    e2.disk = d
    events.append(e1)
    events.append(e2)
# events.sort() # sort the event queue

queu = PriorityQueue(events)
print(queu.events)
while not queu.is_empty():
    e = queu.pop() # get next event
    print(e)


scanline = binaryTree()
scanline.insert(disk[0].x)