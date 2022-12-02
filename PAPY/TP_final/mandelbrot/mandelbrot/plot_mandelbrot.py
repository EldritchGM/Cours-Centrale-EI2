import mandelbrot.mandelbrot as mandelbrot
from numpy import arange
import numpy as np
from PIL import Image
import numba

@numba.jit(nopython=True)
def pixel_coords(x_min, x_max, y_min, y_max, pixel_size, max_iter):
    """
    Renvoie l'ensemble des complexes c dont la partie réelle est comprise entre x_in et x_max
    et la partie imaginaire entre y_min et y_max tels que c appartient à l'ensemble de Mandelbrot

    === Parameters ===
    x_min: float
        borne inférieure de la partie réelle de c
    x_max: float
        borne supérieure de la partie réelle de c
    y_min: float
        borne inférieure de la partie imaginaire de c
    y_max: float
        borne supérieure de la partie imaginaire de c
    pixel_size: float
        pas auquel on fera des tests de convergence de c.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence
    
    === Returns ===
    Re_plot: [float]
        partie réelle de tous les complexes c de l'ensemble de Mandelbrot
    Imag_plot: [float]
        partie imaginaire de tous les complexes z de l'ensemble de Mandelbrot
    """
    Re_list = arange(x_min, x_max, pixel_size)
    Imag_list = arange(y_min, y_max, pixel_size)
    Re_plot = []
    Imag_plot = []
    for x in Re_list:
        for y in Imag_list:
            c = x + y * 1j
            if mandelbrot.is_in_Mandelbrot(c, max_iter):
                Re_plot.append(x)
                Imag_plot.append(y)
    return Re_plot, Imag_plot

@numba.jit(nopython = True)
def matrix_mandelbrot(zmin = - 2 - 2j, zmax =1 + 2j, pixel_size=5e-2,max_iter = 200):
    """
    Renvoie une matrice de triplet RGB représentant chacun un pixel correspondant à un complexe c compris entre zmin et zmax
    Le pixel est noir si c est dans l'ensemble de Mandelbrot, blanc sinon.

    === Parameters ===
    z_min: complex
        borne inférieure de c
    z_max: complex
        borne supérieure de c
    pixel_size: float
        pas auquel on fera des tests de convergence de c.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence

    === Returns ===
    np.array
        Matrice de pixels correspondant à des complexes c: noirs si c est dans l'ensemble de Mandelbrot, blanc sinon 
    """
    x_min, y_min = zmin.real, zmin.imag
    x_max, y_max = zmax.real, zmax.imag
    width = round(abs(x_max - x_min)/pixel_size)
    height = round(abs(y_max - y_min)/pixel_size)

    Re_plot, Imag_plot = pixel_coords(x_min, x_max, y_min, y_max, pixel_size, max_iter)
    
    
    img_matrix = np.full((height, width, 3), fill_value = 255).astype(np.uint8)

    for i in range(len(Re_plot)):
        img_matrix[round((Imag_plot[i]-y_min)/pixel_size) - 1][round((Re_plot[i] - x_min)/pixel_size) - 1] = np.array([0,0,0])
    #img_matrix = img_matrix.astype(np.uint8)
    return img_matrix
    
def plot_mandelbrot(zmin = - 2 - 2j, zmax =1 + 2j, pixel_size=5e-4,max_iter = 200, figname = "test.png"):
    """
    Plot de l'ensemble de Mandelbrot et le sauvegarde sous le nom figname

    === Parameters ===
    zmin: complex
        borne inférieure de c
    zmax: complex
        borne supérieure de c
    pixel_size: float
        pas auquel on fera des tests de convergence de c.
    max_iter: int 
        indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence
    figname: str
        Nom sous lequel le plot sera enregistré
        Peut commencer ou non par le chemin d'accès absolu au fichier. Si absent il sera sauvegardé dans le répertoire courant
    === Returns ===
    None
        Une image est enregistrée
    """
    img_matrix = matrix_mandelbrot(zmin, zmax, pixel_size, max_iter)
    img = Image.fromarray(img_matrix, mode = 'RGB')
    img.save(figname)

if __name__ == "__main__":
    plot_mandelbrot(zmin = - 2 - 2j, zmax = 1 + 2j, pixel_size=5e-4,max_iter = 100, figname = "test.png")
    plot_mandelbrot(zmin=-0.7440+0.1305j, zmax=-0.7425+0.1320j, pixel_size=5e-4, max_iter=200,figname="Mandelbrot_tentacle.png")