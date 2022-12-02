import random as rnd
from sys import getsizeof
class MatCooPure:
    def __init__(self, n, m, n_non_null):
        self.n = n
        self.m = m
        coords = []
        for i in range(n_non_null):
            coord = (rnd.randint(0,(n-1)),rnd.randint(0,(m-1)))
            while coord in coords:
                coord = (rnd.randint(0,n-1),rnd.randint(0,m-1))
            coords.append(coord)
        self.coo = {}
        for coord in coords:
            self.coo[coord] = rnd.random()
    

    @classmethod
    def eye(cls,n):
        mat = MatCooPure(n,n,0)
        for i in range(n):
            mat.coo[(i,i)] = 1
        return mat
    
    def __repr__(self):
        res = f"Matrice COO Pure de dimension {self.n}x{self.m}\n"
        for coord in self.coo:
            res += f"{coord}\t{self.coo[coord]}\n"
        res += f"Mémoire utilisée: {getsizeof(self)}o"
        
        return res

    def mul_naif(self, vect):
        res = []
        for i in range(self.n):
            res.append(0)
            for j in range(self.m):
                if (i,j) in self.coo:
                    aij = self.coo[(i,j)]
                else:
                    aij = 0
                res[-1] += aij * vect[j]
        return res
    

###TEST###
def test_eye():
    M = MatCooPure.eye(3)
    assert M.coo == {(0,0): 1, (1,1): 1, (2,2): 1}
    assert M.m == 3
    assert M.n == 3

def test_print():
    M = MatCooPure.eye(2)
    assert str(M).startswith("Matrice COO Pure de dimension 2x2\n(0, 0)\t1\n(1, 1)\t1\nMémoire utilisée: 48o")

def test_mul_naif():
    vect = [1,1,1]
    M = MatCooPure.eye(3)
    assert M.mul_naif(vect) == [1,1,1]

if __name__ == "__main__":
    test_eye()
    test_print()
    test_mul_naif()
    print("all test passed")