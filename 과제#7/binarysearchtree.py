
class Node:
    def __init__(self,
                 data=None,
                 left=None,
                 right=None,
                 parent=None):
        self._data = data
        self._left = None
        self._right = None
        self._parent = None
        
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, left):
        self._left = left
    
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, right):
        self._right = right
        
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent
        
    def __str__(self):
        return "Node({})".format(self.data)
    
    def __repr__(self):
        return str(self)

    def count_children(self):
        if self._left == None or self._right == None:
            if self._left == None and self._right == None:
                return 0
            else:
                return 1
        else:
            return 2
    def children(self):
        if self._left == None or self._right == None:
            if self._left == None and self._right == None:
                return []
            elif self._left == None:
                return[self._right]
            else:
                return[self._left]                    
        else:
            return[self._left, self._right]

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._num_nodes = 0
    
    def __len__(self):
        return self._num_nodes
    
    def empty(self):
        if self._num_nodes == 0:
            return True
        else:
            return False
    
    def insert(self, data):      
        new_node = Node(data=data)
        
        if self.empty():
            self._root = new_node
            self._num_nodes += 1
            return
            
        cur = self._root
        while cur is not None:
            if data < cur.data:
                if cur.left is None:
                    new_node.parent = cur
                    cur.left = new_node
                    break
                cur = cur._left
            else:
                if cur.right is None:
                    new_node.parent = cur
                    cur._right = new_node
                    break
                cur = cur.right
        self._num_nodes += 1
                
            
    
    def inorder(self, get_node=False):
        if self.empty():
            return []
        if get_node is True:
            l = []
            def inord(cur):
                if cur is None:
                    pass
                else:
                    inord(cur._left)
                    l.append(cur)
                    inord(cur._right)
                return l
            return (inord(self._root))
        l = []
        def inord(cur):
            if cur is None:
                pass
            else:
                inord(cur._left)
                l.append(cur._data)
                inord(cur._right)
            return l
        return(inord(self._root))
    
    def preorder(self, get_node=False):
        if self.empty():
            return []
        if get_node is True:
            l = []
            def pre(cur):
                if cur is None:
                    pass
                else:
                    l.append(cur)
                    pre(cur._left)
                    pre(cur._right)
                return l
            return (pre(self._root))
        l = []
        def pre(cur):
            if cur is None:
                pass
            else:
                l.append(cur._data)
                pre(cur._left)
                pre(cur._right)
            return l
        return(pre(self._root))       
        
                          
    def postorder(self, get_node=False):
        if self.empty():
            return []
        if get_node is True:
            l = []
            def post(cur):
                if cur is None:
                    pass
                else:
                    post(cur._left)
                    post(cur._right)
                    l.append(cur)
                return l
            return (post(self._root))
        l = []
        def post(cur):
            if cur is None:
                pass
            else:
                post(cur._left)
                post(cur._right)
                l.append(cur._data)
            return l
        return(post(self._root))
    
    def min(self, root=None, get_node=False):
        if root is None:
            root = self._root
        while root._left is not None:
            root = root._left
        if get_node is True:
            return root
        return root._data
    
    def max(self, root=None, get_node=False):
        if root is None:
            root = self._root
        while root._right is not None:
            root = root._right      
        if get_node is True:
            return root
        return root._data       
        
    def search(self, data):
        if self.empty():
            raise IndexError
        
        cur = self._root
        while cur is not None:
            if data < cur.data:
                cur = cur.left
            elif data > cur.data:
                cur = cur.right
            else:
                return cur
            
        return None
 
    def remove(self, data):
        if self.empty():
            pass
        else:
            #children = 0
            n = self.search(data)
            if n.left is None and n.right is None:
                if n == self._root:
                    pass
                else:
                    p = n.parent
                    if n == p.left:
                        p.left = None
                    else:
                        p.right = None
                self._num_nodes -= 1
                return n
            #children = only left
            elif n.left is not None and n.right is None:
                lc = n.left
                if n == self._root:
                    self._root = lc
                else:
                    p = n.parent
                    if n == p.left:
                        p.left = lc
                        lc.parent = p
                    else:
                        p.right = lc
                        lc.parent = p
                self._num_nodes -= 1
                return n
            #children = only right
            elif n.left is None and n.right is not None:
                rc = n.right
                if n == self._root:
                    self._root = rc
                else:
                    p = n.parent
                    if n == p.left:
                        p.left = rc
                        rc.parent = p
                    else:
                        p.right = rc
                        rc.parent = p
                self._num_nodes -= 1
                return n
            #children = 2
            else:
                m = self.min(n.right, get_node = True)
                n.data = m.data
                if n.right == m:
                    if m.right is None:
                        n.right = None
                    else:
                        n.right = m.right
                        m.right.parent = n
                else:
                    if m.right is None:
                        m.parent.left = None
                    else:
                        m.parent.left = m.right
                        m.right.parent = m.parent
                self._num_nodes -= 1
                return n

    def clear(self):
        if self.empty():
            return True
        l = self.postorder(get_node=True)     
        for i in l:
            if i._left is not None:
                i._left = None
                self._num_nodes -= 1
            
            if i._right is not None:
                i._right = None
                self._num_nodes -= 1
        self._root = None
        self._num_nodes = 0
        if self._num_nodes == 0:
            return True
        else:
            return False

    
    