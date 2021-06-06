from read_data import read_data
import binary_tree
from event import PriorityQueue, Event
from visualise import plot_problem

# Read the data
rect, disk = read_data('./input2.txt')
# Sort the disks in ascending order by x coordinate
# disk.sort(key=lambda c: c.x, reverse=False)

class PlaneSweep:
    # TODO we are counting intersections of disks outside the rectangle too
    def __init__(self):
        self.tree = binary_tree.BinaryTree() # Init empty binary tree
    
    def add(self, disk):
        '''
        Adds disk to the scanline.
        For each disk you add the upper and lower tangent
        '''

        upper = binary_tree.Node(disk.y + disk.r, disk)
        # if upper.key < rect.y_max:
        binary_tree.tree_insert(self.tree, upper)
        lower = binary_tree.Node(disk.y - disk.r, disk)
        # if lower.key > rect.y_min:
        binary_tree.tree_insert(self.tree, lower)

    def delete(self, disk):
        '''
        Remove disk from the scanline
        For each disk, you must remove the upper and lower tangent
        '''

        # Finds the disk in the binary tree
        # note that this is partially correct. You are indirectly
        # searching for the disk
        upper = binary_tree.tree_find(self.tree.root, disk.y + disk.r)
        # if upper:
        binary_tree.tree_delete(self.tree, upper)

        lower = binary_tree.tree_find(self.tree.root, disk.y - disk.r)
        # if lower:
        binary_tree.tree_delete(self.tree, lower)

    def update(self):
        '''
        At each insertion or deletion we compute the intersction
        of each disk with its neighbour
        '''
        0

def compute_intersection(self):
    '''
    Computes the number of intersections for each interval and the disk
    on the scanlne
    '''


# Initialize planesweep wth disks intersecting the scanline at left boundary of rectangle
planesweep = PlaneSweep()
init_disk = []
for d in disk:
    if d.x - d.r <= rect.x_min:
        init_disk.append(d)
        planesweep.add(d)
        disk.remove(d)
# Init the intersection interval
intersection = []*(len(init_disk)-1)
# for d in init_disk:


# Generate events
events = []
for d in disk:
    # Generate two events for both leftmost and rightmost point of each disk
    e1 = Event()
    e1.val = d.x - d.r
    e1.disk = d
    e1.type = 'left'
    e2 = Event()
    e2.val = d.x + d.r
    e2.disk = d
    e2.type = 'right'
    events.append(e1)
    events.append(e2)
# events.sort() # sort the event queue

queu = PriorityQueue(events)
# print(queu.events)


# while not queu.is_empty():
    # e = queu.pop() # get next event
    # if e.type == 'left':
    #     print('Encountered left event')
    #     planesweep.add(e.disk)
    # elif e.type == 'right':
    #     print('Encountered rigth event')
    #     planesweep.delete(e.disk)
    # elif e.type == 'intersection':
    #     planesweep.update() #TODO?

    # binary_tree.in_order_print(planesweep.tree.root)


# plot_problem(disk, rect, './visualise.png')