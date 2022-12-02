from array import array # On évite ainsi de recourrir à numpy en utilisant un built-in
import math # bien utile pour tout un tas d'opérations
import numbers

class Vecteur:
    def __init__(self, x, y):
        self._x = x * 1.
        self._y = y * 1.
    
    @classmethod
    def from_iterable(cls, it):
        if len(it) < 2:
            raise ValueError("itérable trop court pour un vecteur")
        elif len(it) > 2:
            raise ValueError("itérable trop long pour un vecteur")
        x,y = it
        return Vecteur(x,y)
    
    @classmethod
    def from_polar(cls,r: float, theta: float):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return Vecteur(x, y)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value: numbers.Real):
        if isinstance(value,numbers.Real):  
            self._x = value
        else:
            raise ValueError(f"{value=} doit être un réel")
    
    @y.setter
    def y(self, value: numbers.Real):
        if isinstance(value, numbers.Real):  
            self._y = value
        else:
            raise ValueError(f"{value=} doit être un réel")



    def __repr__(self):
        """Représentation textuelle de l'objet"""
        return(f"Vecteur({self._x},{self._y})")

    def __iter__(self):
        """Iterateur sur les élements du vecteur, utilise yield"""
        for i in (self._x,self._y):
            yield i

    def __str__(self):
        """Appelé par print()"""
        return(f"({self._x},{self._y})")

    def __eq__(self, other):
        """Surcharge de l'opérateur =="""
        type_eq = (type(self) == type(other))
        xeq = (self._x == other._x)
        yeq = (self._y == other._y)
        return (type_eq and xeq and yeq)

    def __abs__(self):
        """surcharge du built-in abs()"""
        return math.sqrt(self._x * self._x + self._y * self._y)
    
    def __add__(self,other):
        """surcharge du +"""
        other = Vecteur.from_iterable(other)
        addx = self._x + other._x
        addy = self._y + other._y
        return Vecteur(addx,addy)
    
    def __sub__(self,other):
        """surcharge du -"""
        subx = self._x - other._x
        suby = self._y - other._y
        return Vecteur(subx,suby)
    
    def __iadd__(self,other):
        self = self + other
    
    def __isub__(self,other):
        self = self - other
    
    def __mul__(self,other):
        if isinstance(other, numbers.Real):
            mulx = self._x * other
            muly = self._y * other
            return Vecteur(mulx, muly)
        elif isinstance(other, Vecteur):
            mulx = self._x * other._x
            muly = self._y * other._y
            return mulx+muly
        else:
            raise ValueError(f"{other} should be a number or a vector")
    
    def __rmul__(self,other):
        return self * other
    
    def __neg__(self):
        return (Vecteur(0,0) - self)

    def __len__(self):
        return 2
    
    def angle(self,other):
        if isinstance(other, Vecteur):
            numer = self * other
            denum = abs(self) * abs(other)
            return numer/denum
        else:
            raise ValueError("angle entre deux vecteurs")


if __name__ == "__main__":
    u = Vecteur(3, 4)
    v = Vecteur(6,8)
    print(u)
    for i in v:
        print(i)
    print(u==v)
    print(abs(u))
    v1 = Vecteur(3, 4)
    print(v1.x, v1.y)  
    x, y = v1 
    print(x, y)
    repr(v1)
    v1_clone = eval(repr(v1))  # la bonne façon de cloner c'est avec copy. Ici on montre l'utilité d'avoir un __repr__ qui écrit l'appel au constructeur de classe combiné avec eval qui evalue un str en python.
    print(v1 == v1_clone)
    print(v1)   
    print(abs(v1))
    from math import pi
    v2=Vecteur.from_iterable([1,5])
    print(v2)
    v2=Vecteur.from_polar(1,pi/4)
    print(v2)
    v3=Vecteur(1,2)
    print(v3.y)
    v3.y=1
    try:
        v3.y="1"
    except Exception as e:
        print("catching exception:", e)
    print(v3)
    print(v1)
    print(v1 + v3)