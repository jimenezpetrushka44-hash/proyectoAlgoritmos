#Importando librerias necesarias

import pygame 
import numpy as np
import random
import heapq
import time #importe esta libreria para medir el tiempo de ejecucion del algoritmo

#Iniciando valores para el maze:
width = 600
height = 600
n = 51
cell = width // n

pygame.init() #Iniciando pygame

btn_start = pygame.Rect(200, 330, 200, 50)
btn_retry = pygame.Rect(20, 550, 150, 40)
btn_details = pygame.Rect(400, 550, 150, 40) #boton para mostrar detalles del algoritmo

start_time = None #iniciando el contador de tiempo
end_time = None #finalizando el contador de tiempo
execution_time = None #variable para guardar el tiempo de ejecucion
mostrar_detalles = False #variable para controlar si se muestran los detalles del algoritmo o no

#paleta de colores para que se vea bonito jiji

bg_soft        = (255, 240, 245)

walls_color    = (180, 50, 120)
path_color     = (255, 255, 255)

visited_color  = (255, 182, 193)
final_path     = (255, 20, 147)

start_color    = (255, 105, 180)
end_color      = (0, 255, 0)

#Variables para implementar mi menu:
estado = "menu"
nombre = ""

font_title = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 25)

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
        
        yield visited, None
        
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
                    
    yield visited, prev
    

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

#ariables nuevas para dijkstra
algo = None
visited = set()
path = None

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if estado == "menu":

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN:
                    estado = "algoritmo"
                else:
                    nombre += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.collidepoint(pygame.mouse.get_pos()):
                    estado = "algoritmo"

        elif estado == "algoritmo":

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_retry.collidepoint(pygame.mouse.get_pos()):
                    maze = np.ones((n,n))
                    generar(1,1)
                    start = None
                    end = None
                    visited = set()
                    path = None
                    algo = None
                    start_time = None
                    end_time = None
                    execution_time = None
                    mostrar_detalles = False

                elif btn_details.collidepoint(pygame.mouse.get_pos()):
                    if path:
                        mostrar_detalles = not mostrar_detalles

                else:
                    x,y = pygame.mouse.get_pos()
                    i, j = y//cell, x // cell
                    
                    if 0 <= i < n and 0 <= j < n:
                        if maze[i][j] == 0:
                            if start is None:
                                start = (i,j)
                            elif end is None:
                                end =(i,j)
                                algo = dijkstra(maze, start, end)
                                start_time = time.perf_counter() #iniciando el tiempo de ejecucion del algoritmo

    if algo:
        try:
            visited, result = next(algo)
            if result:
                path = reconstruir(result, start, end)
                end_time = time.perf_counter() #finalizando el tiempo de ejecucion del algoritmo
                execution_time = end_time - start_time #calculando el tiempo de ejecucion del algoritmo
                algo = None
        except StopIteration:
            algo = None

    if estado == "menu":

        screen.fill((20,30,80))

        title = font_title.render("ALGORITMO DIJKSTRA", True, (255,255,255))
        screen.blit(title, (120,150))

        sub = font_small.render("Bienvenid@", True, (200,200,255))
        screen.blit(sub, (250,190))

        input_box = pygame.Rect(150, 250, 300, 50)
        pygame.draw.rect(screen, (255,255,255), input_box, border_radius=15)

        text = font_small.render(nombre, True, (0,0,0))
        screen.blit(text, (160, 265))

        pygame.draw.rect(screen, (255,105,180), btn_start, border_radius=20)

        txt_btn = font_small.render("START MAZE", True, (255,255,255))
        screen.blit(txt_btn, (225, 345))

    elif estado == "algoritmo":

        screen.fill(bg_soft)

        #Aqui dibujo el maze:
        for i in range(n):
            for j in range(n):
                if maze[i][j] == 1:
                    color = walls_color
                else:
                    color = path_color
                pygame.draw.rect(screen, color, (j*cell, i*cell, cell, cell))

        #dibujar visited
        for (i,j) in visited:
            pygame.draw.rect(screen, visited_color, (j*cell, i*cell, cell, cell))

        #dibujar path
        if path:
            for (i,j) in path:
                pygame.draw.rect(screen, final_path, (j*cell, i*cell, cell, cell))

        #dibujar start y end:
        if start:
            pygame.draw.rect(screen, start_color, (start[1]*cell, start[0]*cell, cell,cell))
        if end:
            pygame.draw.rect(screen, end_color, (end[1]*cell, end[0]*cell, cell, cell))

        pygame.draw.rect(screen, (255,105,180), btn_retry, border_radius=10)
        txt_retry = font_small.render("TRY AGAIN", True, (255,255,255))
        screen.blit(txt_retry, (30, 560))

        pygame.draw.rect(screen, (255,105,180), btn_details, border_radius=10)
        txt_details = font_small.render("SHOW DETAILS", True, (255,255,255))
        screen.blit(txt_details, (410, 560))

        if mostrar_detalles and path:
            pygame.draw.rect(screen, (255,255,255), (20, 20, 360, 120), border_radius=15)
            pygame.draw.rect(screen, (255,105,180), (20, 20, 360, 120), 3, border_radius=15)

            info1 = font_small.render(f"Tiempo: {execution_time:.5f}s", True, (0,0,0))
            info2 = font_small.render(f"Distancia: {len(path)-1}", True, (0,0,0))
            info3 = font_small.render(f"Nodos visitados: {len(visited)}", True, (0,0,0))

            screen.blit(info1, (35, 35))
            screen.blit(info2, (35, 70))
            screen.blit(info3, (35, 105))
                    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()