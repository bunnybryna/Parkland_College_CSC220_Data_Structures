from binary_search_tree import TreeMap

class SplayTreeMap(TreeMap):
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            # zig 
            if grand is None:
                self._roate(p)
            # zig zig 
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            # zig zag
            else:
                self._rotate(p)
                self._rotate(p)
                    
    def _rebalance_insert(self, p):
        self._splay(p)
        
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)
            
    def _rebalance_access(self, p):
        self._splay(p)