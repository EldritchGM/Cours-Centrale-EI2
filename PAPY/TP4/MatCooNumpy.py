import numpy as np
from scipy import sparse
from sys import getsizeof

class MatCooNumpy:
    def __init__(self,n,m,n_non_null):
        self.matrix = sparse.random(n,m, density = n / (m*n), format = 'coo', dtype = 'int8')
        self.n = n
        self.m = m
    
    @classmethod
    def eye(cls,n):
        mat = MatCooNumpy(n, n, 0)
        mat.matrix = sparse.eye(n, format = 'coo')
        return mat
    
    def __repr__(self):
        res = f"Matrice COO Numpy de dimension {self.n}x{self.m}\n" 
        res += str(self.matrix)
        res += f"\nMémoire utilisée: {getsizeof(self)}o"
        return res
    
    def mul(self, vect):
        return np.matmul(self.matrix.toarray(), vect)
    

if __name__ == '__main__':
    print(MatCooNumpy(3,3,4))
    Id = MatCooNumpy.eye(3)
    print(Id)
    print(Id.mul(np.ones(3)))
    print("all test passed")