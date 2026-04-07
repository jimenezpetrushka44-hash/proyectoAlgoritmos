#Este es el codigo de dikjstra

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
        
    
