import math
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


class Value:
    
    def __init__(self, data), _children=(), _op='':
        self.data=data
        self.prev=set(_children)   
        self.op = _op
        
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self,other):
        out = Value(self.data + other.data, (self,other), '+')
        return out
    def __mul__(self,other):
        out = Value(self.data * other.data, (self,other), '*')
        return out