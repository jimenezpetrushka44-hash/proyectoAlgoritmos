#Importando librerias necesarias

import pygame 
import numpy as np
import random
import heapq

#Iniciando valores para el maze:
width = 1000
height = 1000
n = 51
cell = width // n

pygame.init() #Iniciando pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dijkstra Maze")


maze = np.ones((n,n))
dirs = [(-2,0), (2,0), (0,-2), (0,2)]

#Creando funciones para el maze:
def generar(x,y):
    maze[x][y] = 0
    random.shuffle(dirs)
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 1 <= nx < n-1 and 1 <= ny < n-1 and maze[nx][ny] ==1:
            maze[x + dx//2][y + dy//2] = 0
            generar(nx, ny)
generar(1,1)


    

#Funcion para dijkstra:
def dijkstra(maze, start, end):
    n=len(maze)
    pq=[(0, start)]
    dist = {start:0}
    prev = { }
    visited = set()
    
    while pq:
        d, (x,y) = heapq.heappop(pq)
        visited.add((x,y))
        
        yield visited, None #animacion de los nodos recorridos
        
        if (x,y) == end:
            break
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
                new_d = d+1
                if(nx,ny) not in dist or new_d < dist[(nx,ny)]:
                    dist[(nx,ny)] = new_d
                    prev[(nx,ny)] = (x,y)
                    heapq.heappush(pq, (new_d, (nx,ny)))
                    
    return prev                
    

#Reconstruyendo el path:
def reconstruir(prev, start, end):
    path = []
    cur = end 
    while cur in prev:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()
    
    return path

 
running = True

#Click del usuario (start y end en el maze)

start = None
end = None

while running:
    for event in pygame.event.get():
        


        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            i, j = y//cell, x // cell
            
            if maze[i][j] == 0:
                if not start:
                    start = (i,j)
                elif not end:
                    end =(i,j)
            
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))
    
    #Aqui dibujo el maze:
    for i in range(n):
        for j in range(n):
            color = (255, 255,255)
            if maze[i][j] == 0:
                color = (0,0,0)
            pygame.draw.rect(screen, color, (j*cell, i*cell, cell, cell))
            if start:
                pygame.draw.rect(screen, (0,255,0), (start[1]*cell, start[0]*cell, cell,cell))
            if end:
                pygame.draw.rect(screen, (225,255,0), (end[1]*cell, end[0]*cell, cell, cell))
                    
    pygame.display.flip()
    
pygame.quit()

