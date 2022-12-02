from mandelbrot.plot_mandelbrot import plot_mandelbrot
from mandelbrot.plot_julia import plot_julia
import argparse
import time

def mandelbrot():
    parser = argparse.ArgumentParser(description=plot_mandelbrot.__doc__)
    parser.add_argument('--z_min', '-zm', metavar = "z_min", type = complex, help = "borne inférieure de c", default = - 2 - 2j)
    parser.add_argument('--z_max', '-zM', metavar = "z_max", type = complex, help = "borne inférieure de c", default = 1 + 2j)
    parser.add_argument('--pixel_size', '-spx', metavar= "pixel_size", type = float, help = "pas auquel on fera des tests de convergence de z.", default = 5e-4)
    parser.add_argument('--iter', '-i', metavar= "max_iter", type = int, help = "indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence", default = 200)
    parser.add_argument('--name', '-n', metavar= "fig_name", type = str, help = "Nom sous lequel le plot sera enregistré", default = "test.png")

    args = parser.parse_args()
    z_min, z_max, pixel_size, max_iter, fig_name = args.z_min, args.z_max, args.pixel_size, args.iter, args.name
    
    plot_mandelbrot(z_min, z_max, pixel_size, max_iter, fig_name)

def julia():
    parser = argparse.ArgumentParser(description=plot_julia.__doc__)
    parser.add_argument('--c', '-c', metavar= 'c', type = complex, help = "Paramètre imposé pour l'ensemble de Julia", default = None)
    parser.add_argument('--z_min', '-zm', metavar = "z_min", type = complex, help = "borne inférieure de z", default = - 2 - 2j)
    parser.add_argument('--z_max', '-zM', metavar = "z_max", type = complex, help = "borne inférieure de z", default = 1 + 2j)
    parser.add_argument('--pixel_size', '-spx', metavar= "pixel_size", type = float, help = "pas auquel on fera des tests de convergence de z.", default = 5e-4)
    parser.add_argument('--iter', '-i', metavar= "max_iter", type = int, help = "indique le nombre maximal d'itérations que l'on regarde pour conclure sur la convergence", default = 200)
    parser.add_argument('--name', '-n', metavar= "fig_name", type = str, help = "Nom sous lequel le plot sera enregistré", default = "test.png")

    args = parser.parse_args()
    c, z_min, z_max, pixel_size, max_iter, fig_name = args.c, args.z_min, args.z_max, args.pixel_size, args.iter, args.name
    if c == None:
        raise ValueError("You have to give the c parameter")
    
    plot_julia(c, z_min, z_max, pixel_size, max_iter, fig_name)    




if __name__ == "__main__":
    before = time.time()
    plot_mandelbrot(zmin = - 2 - 2j, zmax = 1 + 2j, pixel_size=5e-4,max_iter = 100, figname = "test.png")
    plot_mandelbrot(zmin=-0.7440+0.1305j, zmax=-0.7425+0.1320j, pixel_size=5e-7, max_iter=200,figname="Mandelbrot_tentacle.png")
    plot_julia(c=-0.8 + 0.156j,zmin=-2-1j,zmax=2+1j,pixel_size=5e-4,max_iter=100,figname="Julia_-0.8+0.156j.png")
    after = time.time()
    print(f"Fin d'exécution\nTemps d'execution: {after - before}s")