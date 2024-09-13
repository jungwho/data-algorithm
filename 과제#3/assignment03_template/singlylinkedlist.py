
class Node(object):
    
    def __init__(self, data=None):
        
        self._data = data
        self._next = None
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
        
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, n):
        self._next = n
    
class SinglyLinkedList(object):
    
    def __init__(self):
        
        self._head = None
        self._tail = None
        self._num_nodes = 0
        
        
    def __str__(self):
        if self.empty():
            return "[]"
        else:
            tmp_list = []  # Temporary list of strings
            cur = self._head            
            while cur != None:
                tmp_list.append("[%s]"%(cur.data))
                cur = cur.next
        
            return "->".join(tmp_list)
        
    def __len__(self):
        
        return self._num_nodes
            
    def empty(self):
        
        if (self._num_nodes == 0):
            return True
        else:
            return False
        
        
    def insert(self, i, data):
        
        new_node = Node(data)
        
        if (i<0 or i>self._num_nodes):
            raise IndexError
            
        elif self.empty():
            self._head = new_node
            self._tail = new_node
            self._num_nodes = 1
                
        elif (i == self._num_nodes):
            self._tail._next = new_node
            self._tail = self._tail._next
            self._num_nodes += 1
            
        elif (i == 0):
            new_node._next = self._head
            self._head = new_node
            self._num_nodes += 1
                
        else:
            cur = self._head
            for j in range(i-1):
                cur = cur._next
            pre = cur
            aft = cur._next
            
            pre._next = new_node
            new_node._next = aft
            self._num_nodes += 1
                
    def remove(self, i):
        cur = self._head
        if self.empty():
            pass     

        elif (i<0 or i>=self._num_nodes):
            raise IndexError
        
        elif (self._num_nodes == 1):
            self._head = None
            self._tail = None
            self._num_nodes = 0
            
        elif (i == 0):
            self._head = self._head._next
            self._num_nodes -= 1
            
        elif (i+1 == self._num_nodes):
            for j in range(i-1):
                cur = cur._next
            self._tail = cur
            self._num_nodes -= 1
            
        else:            
            for j in range(i-1):
                cur = cur._next
            x = cur._next
            aft = x._next
            cur._next = aft
            self._num_nodes -= 1
            
            
              
    def clear(self):
        
        if self.empty():
            pass
        
        else:
            a = self._head
            b = a._next
            b = b._next
            for i in range(self._num_nodes - 3):               
                a._next = b
                self._num_nodes -= 1
                b=b._next
            
            self._head = None
            self._tail = None
            self._num_nodes = 0
                
    def get(self, i):
        
        if self.empty():
            raise IndexError
        
        elif (i<0 or i>self._num_nodes):
            raise IndexError
            
        else:
            cur = self._head
            for j in range(i):
                cur = cur._next
            return cur._data
    
    def pop(self, i=None):  
        cur = self._head
        if self.empty():
            raise IndexError          
        
        elif (i is None):
            d = self._tail._data
            if self._num_nodes == 1:
                self._head = None
                self._tail = None
                self._num_nodes -= 1
            else:
                for j in range(self._num_nodes - 2):
                    cur = cur._next
                self._tail = cur
                self._num_nodes -= 1
            return d
        
        elif (i<0 or i>=self._num_nodes):
            raise IndexError
        
        elif (i == 0):
            d = self._head._data
            if self._num_nodes == 1:
                self._head = None
                self._tail = None
                self._num_nodes -= 1
                
            else:
                self._head = self._head._next
                self._num_nodes -= 1     
            return d
        
        elif (i+1 == self._num_nodes):
            d = self._tail._data
            for j in range(i-1):
                cur = cur._next
            self._tail = cur
            self._num_nodes -= 1
            return d
        
        else:            
            for j in range(i-1):
                cur = cur._next
            x = cur._next
            aft = x._next
            cur._next = aft
            self._num_nodes -= 1
            return x._data
            
    
    def search(self, target, start=0):
        
        if self.empty():
            raise IndexError
        
        elif (start<0 or start>=self._num_nodes):
            raise IndexError
        
        else:
            cur = self._head
            for i in range(start):
                cur = cur._next
                
            while start<=self._num_nodes :
                if (cur._data == target):
                    return cur._data, start
                cur = cur._next
                start += 1
                if (start==self._num_nodes):
                    return None, -1
                 
        
    
    def extend(self, sll):

        if not isinstance (sll, SinglyLinkedList):
            raise TypeError
        
        elif sll.empty():
            pass
        
        else:
            n = sll._num_nodes
            cur = sll._head
            for i in range(n-1):
                self.insert(self._num_nodes, cur._data)
                cur = cur._next
            self.insert(self._num_nodes, cur._data)
            