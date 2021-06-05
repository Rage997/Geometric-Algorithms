'''
I've spent a ridicolous amount of time searching for
a ready to use BSC implementation in python. Scipy does
not have it and I don't know of any other library. However
the only operations I need to have are insertion and deletion
therefore It takes less time to implement it from scratch
The code is taken from the bible aka:
    "Introduction to Algorithms, T. H Cormen et al, CH 12"

My implementation is a little "tricky" because I honestly rushed it
and didn't care too much about code reusability. Sometimes the function
expected a node, otherwise the whole tree.
'''

class Node:
    '''A node of a binary tree'''
    def __init__(self, key, obj=None):
        self.key = key 
        self.left = None
        self.right = None
        self.p = None
        if obj:
            self.obj = obj
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        # self.parent = 

def tree_insert(T, z):
    '''The procedure takes insert a node z into a binary tree T'''

    y = None
    x = T.root
    # Find where to insert
    while x:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    # Acutal insertion
    z.p = y
    if y == None:
        T.root = z # tree empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    if not u.p:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v:
        v.p = u.p

def tree_minimum(z):
    if not z.left:
        return z
    else:
        while z.left:
            z = z.left
        return z

def tree_find(root, key):
    if not root:
        return None
    if key < root.key:
        return tree_find(root.left, key)
    elif key > root.key:
        return tree_find(root.right, key)
    else:
        return root

def tree_delete(T, z):
    '''Deletes a node z with given key from a tree T'''
    if not z.left:
        transplant(T, z, z.right)
    elif not z.right:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y

def in_order_print(root):
    '''Prints elements of the tree in ascending oreder'''
    if not root:
        return
    in_order_print(root.left)
    print (root.key)
    in_order_print(root.right)


def test():
    '''
    I know that this is not the proper way of doing testing
    i.e. no assertion no big data testing but time is a luxury.
    I tested some trivial cases and it worked fine.
    '''
    r = BinaryTree() # empty root
    tree_insert(r, Node(42))
    tree_insert(r, Node(7, obj=5))
    tree_insert(r, Node(1))
    tree_insert(r, Node(5))

    in_order_print(r.root)

    print('--------')
    z = tree_find(r.root, 5)
    tree_delete(r, z)

    in_order_print(r.root)

    print('--------')
    import random
    r = BinaryTree() # empty root
    for i in range(0, 10):
        tree_insert(r, Node(i))

    in_order_print(r.root)

    print('--------')
    for i in range(3, 5):
        z = tree_find(r.root, i)
        tree_delete(r, z)
    
    in_order_print(r.root)

# test()