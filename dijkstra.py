#Este es el codigo de dikjstra

import heapq

#Creando la clase:
class Dijkstra():
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        
    def run(self, start, end):
        dist = { }
        dist[start] = 0 
        prev = { }
        priority_queue = [(0, start)]
        
        #Mientras haya nodos por visitar:
        while priority_queue:            
            current_dist, (x,y) = heapq.heappop(priority_queue) #Saca el nodo menor, mas bajo
            if (x,y) == end:
                break
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            #Aqui recorro todas las direcciones y calculo nuevo nodo:
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < self.n and 0 <= ny < self.n and self.maze[nx][ny] == 0:
                    
        
