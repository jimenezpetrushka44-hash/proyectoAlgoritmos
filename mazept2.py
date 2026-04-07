#Codigo q estoy probando para generar laberintos en python:

#Importando recursos necesarios:

import numpy as np
import matplotlib.pyplot as plt
import random
import time

n = 15
maze= np.ones((n,n))

dirs =[(-2, 0), (2,0), (0,-2), (0,2)]

#Metodo para generar el maze:
def generar(x,y):
    maze[x,y] = 0
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and maze[nx, ny] == 1:
            maze[x + dx // 2, y + dy //2]=0
            generar(nx,ny)
            plt.imshow(maze, cmap="binary")
            plt.axis("off")
            plt.pause(0.5)
            
plt.figure(figsize=(5,5))
generar(0,0)
plt.title("Generador de Mazes - Anna", fontsize=10)
plt.show()