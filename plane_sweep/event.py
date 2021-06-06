class Event:
    '''
    Event struct. There are 3 kind of event:
        1. right
        2. left
        3. intersection
    An event may refer to a disk.
    '''
    val = 0
    disk = None
    kind = None
    
class PriorityQueue:
    '''All operations are in O(n)'''
    def __init__(self, events:[]):
        self.events = events
        self.events.sort(key=lambda e: e.val, reverse=False)

    def insert(self, e):
        for idx, e2 in enumerate(self.events):
            if e < e2:
                # print(e2)
                self.events.insert(idx, e)
                break

    def remove(self, e):
        self.events.remove(e)

    def pop(self):
        e0 = self.events[0]
        self.events.remove(e0)
        return e0

    def is_empty(self):
        return not len(self.events) > 0