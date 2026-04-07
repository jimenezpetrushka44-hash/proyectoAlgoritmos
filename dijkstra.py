#Este es el codigo de dikjstra

import heapq

#Creando la clase:
class Dijkstra():
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
    
    #Metodo q guaarda al algortimo en si
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
            
            #Aqui le doy los pesos, de donde va y para dnd llega
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            #Aqui recorro todas las direcciones y calculo nuevo nodo:
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                #Valido si la ruta es mas corta o larga, actualizo los pesos si se debe
                if 0 <= nx < self.n and 0 <= ny < self.n and self.maze[nx][ny] == 0:
                    new_dist = current_dist + 1
                    
                    #Aqui se actualiza:
                    if (nx, ny) not in dist or new_dist < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_dist
                        prev[(nx,ny)] = (x,y)
                        heapq.heappush(priority_queue, (new_dist, (nx,ny)))
                    
        #Para retornar el path
        path = [ ]
        node = end
        if end not in prev:
            return [ ]
        while node in prev:
            path.append(node)
            node = prev[node]
        path.append(start)
        path.reverse()
        return path
    
#Haciendo testing con un maze q me dio chatgpt
def main():
    maze = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]

    user_input = input("Quieres ver a dijkstra jeje?: ")
        
    if user_input.capitalize() == "Yes":
        
        obj_maze = Dijkstra(maze)
        start = (1,1)
        end= (len(maze)-2, len(maze)-2)
        
        path = obj_maze.run(start,end)
        
        print(f"La ruta mas eficiente segun el algoritmo de Dijkstra es: {path}")
        
        
        
if __name__ == "__main__":
    main()
        
