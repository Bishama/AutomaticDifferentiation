import math
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


class Value:
    
    def __init__(self, data):
        self.data=data
        
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self,other):
        out = Value(self.data + other.data)
        return out
    def __mul__(self,other):
        out = Value(self.data * other.data)
        return out