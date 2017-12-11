from linked_queue import LinkedQueue
import collections

class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
            
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not(self == other)
            
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
        
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
        
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
        
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
        
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
        
    def is_empty(self):
        return len(self) == 0
        
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
            
    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
        
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        # check all p's children, linear time
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
            
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)
        
    def __iter__(self):
        for p in self.positions():
            yield p.element()
            
    def positions(self):
        return self.preorder()
        
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p 
    
    def _subtree_preorder(self, p):
        # visit p before its subtrees
        yield p
        # for each child c
        for c in self.children(p):
            # do preorder of c's subtree
            for other in self._subtree_preorder(c):
                yield other
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
                
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        # visit p after its subtrees
        yield p
        
    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            # start with root, push it to the back
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                # remove from the front
                p = fringe.dequeue()
                yield p 
                # push more from the back
                # it will remove from the top tier then go the lowest (leaf)
                for c in self.children(p):
                    fringe.enqueue(c)
                    