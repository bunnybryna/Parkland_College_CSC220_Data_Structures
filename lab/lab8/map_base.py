from collections import MutableMapping

class MapBase(MutableMapping):
    # nested class
    class _Item:
      #__slots__ tells Python not to use a dict, and only allocate space for a fixed set of attributes to help you save up space 
        __slots__ = '_key', '_value'
        def __init__ (self, k, v):
            self._key = k
            self._value = v
            
        def __eq__(self, other):
            return self._key == other._key
            
        def __ne__(self, other):
            return not (self == other)
            
        def __lt__(self, other):
            return self._key < other._key
            
            