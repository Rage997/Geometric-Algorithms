'''
I've spent a ridicolous amount of time searching for
a ready to use BSC implementation in python. Scipy does
not have it and I don't know of any other library. However
the only operations I need to have are insertion and deletion
therefore It takes less time to implement it from scratch
'''

class binaryTree():
    def __init__(self):
        self.val = None # if None then it's root
        self.left = None
        self.right = None

    def insert(self,val):
        if (self.val == None):
            self.val = val
        else:
            if (val < self.val):
                if(self.left):
                    self.left.insert(val) # recursively insert
                else: 
                    self.left = binaryTree(val)

            # this also cover the casse for val = self.val
            else:
                if(self.right):
                    self.right.insert(val)
                else: self.right = binaryTree(val)
    
    def delete(self, val):
        0 # TODO