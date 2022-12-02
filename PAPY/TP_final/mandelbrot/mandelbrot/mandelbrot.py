import doctest
import numba

@numba.jit(nopython=True)
def suite(z,c)-> complex:
    """Générateur des éléments de la suite z_{n+1}=z_n^2+c$
    
    cf yield Chapitre 2
    
    === Parameters ===
    z : complex
        z_0 paramètre de départ de la suite
    c : complex
        paramètre de départ de la suite
    
    === Returns ===
    Iterateur de la suite.
    
    """
    while True:
        yield z
        z = z ** 2 + c

@numba.jit(nopython=True)
def suite_mandelbrot(c, z=0):
    """Renvoie la suite de Mandelbrot 

    === Parameters ===
    c: complex 
        candidat
    z: complex
        le paramètre d'initialisation. Dans la définition de la suite de Mandelbrot, z_0 = 0

    === Returns ===
    Iterateur de la suite
    """
    return suite(z,c)

@numba.jit(nopython=True)
def suite_julia(z,c):
    """Renvoie la suite de julia pour candidat et parametre

    === Parameters ===
    z: complex
        le candidat
    c: complex
        paramètre fixé de la suite
    
    === Returns ===
    Iterateur de la suite
    """
    return suite(z,c)

@numba.jit(nopython=True)
def is_in_Mandelbrot(c, max_iter = 10):
    """
    Renvoie True si c est dans Mandelbrot, False sinon

    === Parameters === 
    c: complex
        le candidat
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence
    
    === Returns ===
    Bool
        c est-il dans Mandelbrot

    === Tests ===
    >>> is_in_Mandelbrot(c=0.251)
    True
    >>> is_in_Mandelbrot(c=0.251,max_iter=100)
    False
    """
    suite = suite_mandelbrot(c)
    iter = 0
    for z in suite:
        if abs(z) > 3: # l'ensemble de Mandelbrot est contenu dans le cercle complexe de rayon 2.
            return False
        if iter >= max_iter:
            return True
        iter += 1

@numba.jit(nopython=True)
def is_in_Julia(z, c, max_iter = 100):    
    """
    Renvoie True si le coupe (z,c) est dans Julia, False sinon

    === Parameters ===
    z: complex
        z du candidat (z,c)
    c: complex
        c du candidat (z,c)
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence

    === Returns ===
    Bool
        le couple (z,c) est -il dans l'ensemble de Julia

    === Tests ===
    >>> is_in_Julia(z=0.25+0.25j,c=0.25)
    True
    """
    suite = suite_julia(z,c)
    iter = 0
    for z in suite:
        if abs(z) > 3: #l'ensemble de Mandelbrot est contenu dans le cercle complexe de rayon 2.
            return False
        if iter > max_iter:
            return True
        iter += 1    

if __name__ == "__main__":
    print(doctest.testmod())