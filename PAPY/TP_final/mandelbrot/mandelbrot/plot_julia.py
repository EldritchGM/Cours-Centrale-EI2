import mandelbrot.mandelbrot as mandelbrot
from numpy import arange
import numpy as np
from PIL import Image
import numba

@numba.jit(nopython = True)
def pixel_coords(c, x_min, x_max, y_min, y_max, pixel_size, max_iter):
    """
    Renvoie l'ensemble des complexes z dont la partie réelle est comprise entre x_in et x_max
    et la partie imaginaire entre y_min et y_max tels que le couple (z, c) appartient à l'ensemble de Julia

    === Parameters ===
    c : complex 
        Paramètre imposé pour l'ensemble de Julia
    x_min: float
        borne inférieure de la partie réelle de z
    x_max: float
        borne supérieure de la partie réelle de z
    y_min: float
        borne inférieure de la partie imaginaire de z
    y_max: float
        borne supérieure de la partie imaginaire de z
    pixel_size: float
        pas auquel on fera des tests de convergence de z.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence
    
    === Returns ===
    Re_plot: [float]
        partie réelle de tous les complexes z de l'ensemble de Julia
    Imag_plot: [float]
        partie imaginaire de tous les complexes z de l'ensemble de Julia
    """
    Re_list = arange(x_min, x_max, pixel_size)
    Imag_list = arange(y_min, y_max, pixel_size)
    Re_plot = []
    Imag_plot = []
    for x in Re_list:
        for y in Imag_list:
            z = x + y * 1j
            if mandelbrot.is_in_Julia(z, c, max_iter):
                Re_plot.append(x)
                Imag_plot.append(y)
    return Re_plot, Imag_plot

@numba.jit(nopython = True)
def matrix_julia(c, zmin = - 2 - 2j, zmax =1 + 2j, pixel_size=5e-2,max_iter = 200):
    """
    Renvoie une matrice de triplet RGB représentant chacun un pixel correspondant à un complexe z compris entre zmin et zmax
    Le pixel est noir si z est dans l'ensemble de Julia, blanc sinon.

    === Parameters ===
    c : complex 
        Paramètre imposé pour l'ensemble de Julia
    z_min: complex
        borne inférieure de z
    z_max: complex
        borne supérieure de z
    pixel_size: float
        pas auquel on fera des tests de convergence de z.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence

    === Returns ===
    np.array
        Matrice de pixels correspondant à des complexes z: noirs si z est dans l'ensemble de Julia, blanc sinon 
    """
    x_min, y_min = zmin.real, zmin.imag
    x_max, y_max = zmax.real, zmax.imag
    width = round(abs(x_max - x_min)/pixel_size)
    height = round(abs(y_max - y_min)/pixel_size)

    Re_plot, Imag_plot = pixel_coords(c, x_min, x_max, y_min, y_max, pixel_size, max_iter)
    
    
    img_matrix = np.full((height, width, 3), fill_value = 255).astype(np.uint8)

    for i in range(len(Re_plot)):
        img_matrix[round((Imag_plot[i]-y_min)/pixel_size)][round((Re_plot[i] - x_min)/pixel_size)] = np.array([0,0,0])
    img_matrix = img_matrix.astype(np.uint8)
    return img_matrix
    
def plot_julia(c, zmin = - 2 - 2j, zmax =1 + 2j, pixel_size=5e-2,max_iter = 200, figname = "test.png"):
    """
    Plot de l'ensemble de Julia et le sauvegarde sous le nom figname

    === Parameters ===
    c : complex 
        Paramètre imposé pour l'ensemble de Julia
    z_min: complex
        borne inférieure de z
    z_max: complex
        borne supérieure de z
    pixel_size: float
        pas auquel on fera des tests de convergence de z.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence
    figname: str
        Nom sous lequel le plot sera enregistré
        Peut commencer ou non par le chemin d'accès absolu au fichier. Si absent il sera sauvegardé dans le répertoire courant
    === Returns ===
    None
        Une image est enregistrée
    """
    img_matrix = matrix_julia(c, zmin, zmax, pixel_size, max_iter)
    img = Image.fromarray(img_matrix, mode = 'RGB')
    img.save(figname)


if __name__ == "__main__":
    plot_julia(c=-0.8 + 0.156j,zmin=-2-1j,zmax=2+1j,pixel_size=5e-4,max_iter=100,figname="Julia_-0.8+0.156j.png")