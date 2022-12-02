import doctest
from pydoc import doc
import numpy as np
import numba
from PIL import Image
import os
import time
#import cli.app

# Définition des suites
@numba.jit(nopython=True)
def suite(z,c)-> complex:

    """Générateur des éléments de la suite z(n+1)=z(n)^2+c"""

    while True:
        yield z
        z = z ** 2 + c

@numba.jit(nopython=True)
def suite_mandelbrot(c):
    """Renvoie la suite de Mandelbrot générée avec le candidat c

    Parametres :
    ------------
    c : candidat
    """
    return suite(0,c)

@numba.jit(nopython=True)
def suite_julia(z,c):
    """Renvoie la suite de julia pour un candidat et un parametre

    Parametres :
    ------------
    z : candidat
    c : paramètre fixé
    """
    return suite(z,c)

@numba.jit(nopython=True)
# Fonctions d'appartenances aux ensembles de Mandelbrot ou de Julia
def is_in_Mandelbrot(c, max_iter = 10):
    """Renvoie True si le candidat est dans l'ensemble de Mandelbrot et False sinon
    Paramètres :
    ------------
    c : candidat
    max_ietr : nombre d'itération maximum a faire

    Tests :
    ------------
    >>> is_in_Mandelbrot(c=0.251)
    True
    >>> is_in_Mandelbrot(c=0.251,max_iter=100)
    False
    """
    suite = suite_mandelbrot(c)
    iter = 0
    for z in suite:
        if abs(z.real**2) > 2 or abs(z.imag) > 2 :
            return False
        if iter >= max_iter:
            return True
        iter += 1

@numba.jit(nopython=True)
def is_in_Julia(z,c, max_iter = 10):
    """Renvoie True si le couple (z,c) appartient a l'ensemble de Julia et False sinon
    
    Paramètres :
    ------------
    z : z0, paramètre fixé
    c : candidat
    
    Tests :
    ------------
    >>> is_in_Julia(z=0.25+0.25j,c=0.25)
    True
    """
    suite = suite_julia(z,c)
    iter = 0
    for z in suite:
        if abs(z) > 10:
            return False
        if iter >= max_iter:
            return True
        iter += 1

# Récupération des candidats pour l'image
@numba.jit(nopython=True)
def get_c_Mandelbrot(zmin, zmax, pixel_size, max_iter = 10):
    """Renvoie une matrice de triplet RGB ou les candidats présents dans l'ensembles sont noirs

    Paramètres :
    ------------
    zmin : nombre min de l'ensemble cherché
    zmax : nombre max de l'ensemble cherché
    pixel_size = taille des pixels
    max_iter : itération maximale pour le test d'appartenances a l'ensemble
    """
    x_min = zmin.real
    x_max = zmax.real
    width = round(abs(x_max-x_min)/pixel_size)

    y_min = zmin.imag
    y_max = zmax.imag
    height = round(abs(y_max-y_min)/pixel_size)

    X = np.arange(x_min, x_max, pixel_size)
    Y = np.arange(y_min, y_max, pixel_size)

    X_plot = []
    Y_plot = []

    for x in X:
        for y in Y:
            c = x + y * 1j
            if is_in_Mandelbrot(c, max_iter):
                X_plot.append(x)
                Y_plot.append(y)

    img_nb = np.full(shape = (height, width, 3), fill_value = 255).astype(np.uint8)

    for i in range(len(X_plot)):
        img_nb[round((Y_plot[i]-y_min)/pixel_size)-1][round((X_plot[i]-x_min)/pixel_size)-1] = np.array([0,0,0])

    return img_nb

@numba.jit(nopython=True)
def get_c_Julia(c, zmin, zmax, pixel_size, max_iter = 10):
    """Renvoie une matrice de triplet RGB ou les candidats présents dans l'ensembles sont noirs

    Paramètres :
    ------------
    c : paramètre fixé par l'utilisateur
    zmin : nombre min de l'ensemble cherché
    zmax : nombre max de l'ensemble cherché
    pixel_size = taille des pixels
    max_iter : itération maximale pour le test d'appartenances a l'ensemble
    """
    x_min = zmin.real
    x_max = zmax.real
    width = round(abs(x_max-x_min)/pixel_size)

    y_min = zmin.imag
    y_max = zmax.imag
    height = round(abs(y_max-y_min)/pixel_size)

    X = np.arange(x_min, x_max, pixel_size)
    Y = np.arange(y_min, y_max, pixel_size)

    X_plot = []
    Y_plot = []

    for x in X:
        for y in Y:
            z = x + y * 1j
            if is_in_Julia(z, c, max_iter):
                X_plot.append(x)
                Y_plot.append(y)

    img_nb = np.full(shape = (height, width, 3), fill_value = 255).astype(np.uint8)

    for i in range(len(X_plot)):
        img_nb[round((Y_plot[i]-y_min)/pixel_size)-1][round((X_plot[i]-x_min)/pixel_size)-1] = np.array([0,0,0])

    return img_nb

# Plot des ensembles
def plot_mandelbrot(zmin = -2 - 1j, zmax = 1 + 1j, pixel_size = 5e-4, max_iter = 200, figname = "mandelbrot_fractal.png"):
    """Plot l'ensemble de Mandelbrot entre zmin et zmax

    Paramètres :
    ------------
    zmin : nombre min de l'ensemble cherché
    zmax : nombre max de l'ensemble cherché
    pixel_size = taille des pixels
    max_iter : itération maximale pour le test d'appartenances a l'ensemble
    figname : nom de la figure enregistrée
    """

    path = os.getcwd() # On récupère le répertoire courant

    img_nb = get_c_Mandelbrot(zmin, zmax, pixel_size, max_iter) # On récupère les éléments de l'ensemble dans l'intervalle

    fig = Image.fromarray(img_nb, mode = "RGB")
    fig.save(path + figname)  # On enregistre l'image dans le repertoire courant

def plot_julia(c, zmin = -2 - 1j, zmax = 1 + 1j, pixel_size = 5e-4, max_iter = 200, figname = "julia_fractal.png"):
    """Plot l'ensemble de Julia entre zmin et zmax

    Paramètres :
    ------------
    c : paramètre fixé par l'utilisateur
    zmin : nombre min de l'ensemble cherché
    zmax : nombre max de l'ensemble cherché
    pixel_size = taille des pixels
    max_iter : itération maximale pour le test d'appartenances a l'ensemble
    figname : nom de la figure enregistrée
    """
    path = os.getcwd()

    img_nb = get_c_Julia(c, zmin, zmax, pixel_size, max_iter)
    
    fig = Image.fromarray(img_nb, mode = "RGB")
    fig.save(path + figname)


if __name__ == "__main__":
    before = time.time()
    plot_mandelbrot(zmin = - 2 - 2j, zmax = 1 + 2j, pixel_size=5e-4,max_iter = 100, figname = "test.png")
    plot_mandelbrot(zmin=-0.7440+0.1305j, zmax=-0.7425+0.1320j, pixel_size=5e-7, max_iter=200,figname="Mandelbrot_tentacle.png")
    plot_julia(c=-0.8 + 0.156j,zmin=-2-1j,zmax=2+1j,pixel_size=5e-4,max_iter=100,figname="Julia_-0.8+0.156j.png")
    after = time.time()
    print(f"Fin d'exécution\nTemps d'execution: {after - before}s")