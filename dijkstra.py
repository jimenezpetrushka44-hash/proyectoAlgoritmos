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
        
