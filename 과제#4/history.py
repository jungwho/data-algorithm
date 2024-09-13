
class History(object):
    def __init__(self):
        
        self._stack_undo = list()
        self._stack_redo = list()
    
    def __str__(self):
        str_undo_stack = '[]'
        str_redo_stack = '[]'
        if self._stack_undo:
            str_undo_stack = ''.join(['[%s]'%(st) for st in self._stack_undo])        
        if self._stack_redo:
            str_redo_stack = ''.join(['[%s]'%(st) for st in self._stack_redo])        
        return "CURRENT: %s\nUNDO: %s\nREDO: %s"%(self.current_state,
                                                  str_undo_stack,
                                                  str_redo_stack)
    
    @property
    def current_state(self):
        if not self._stack_undo:
            return None
        else:
            return self._stack_undo[-1]       
    
    def undo(self):
        if not self._stack_undo:
            pass
        else:
            self._stack_redo.append(self._stack_undo[-1])         
            self._stack_undo.pop()
    
    def redo(self):
        if not self._stack_redo:
            pass
        else:            
            self._stack_undo.append(self._stack_redo[-1])
            self._stack_redo.pop()
    def append(self, state):
        self._stack_undo.append(state)
        self._stack_redo.clear()
    
    def clear(self):
        self._stack_undo.clear()
        self._stack_redo.clear()
