from map_base import MapBase
from collections import MutableMapping
from random import randrange

class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        # number of entreis in the map
        self._n = 0
        self._prime = p 
        # _scale = a, _shift = b, len(table) = m
        # H = ((ax+b)mod p) mod m
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
        
    def _hash_function(self, k):
        # hash() is a Python built-in method, returns its hash value
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)
        
    def __len__(self):
        return self._n 
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)
        
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        # load factor = n/m, keep it <= 0.5
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
    
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1
        
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        # n will be recomputed during the adds
        self._n = 0
        for (k,v) in old:
            self[k] = v
