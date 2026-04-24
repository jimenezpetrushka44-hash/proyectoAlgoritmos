#Este es el codigo de dikjstra

import heapq
import time
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

    #Metodo nuevo para mostrar el detalle completo y medir el tiempo del algoritmo
    def run_with_details(self, start, end):
        start_time = time.perf_counter()
        dist = {start: 0}
        prev = { }
        priority_queue = [(0, start)]
        visited = set()
        visited_order = [ ]

        while priority_queue:
            current_dist, (x, y) = heapq.heappop(priority_queue)

            #Evita procesar nodos repetidos y guarda el orden real de visita
            if (x, y) in visited:
                continue

            visited.add((x, y))
            visited_order.append((x, y))

            if (x, y) == end:
                break

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.n and 0 <= ny < self.n and self.maze[nx][ny] == 0:
                    new_dist = current_dist + 1

                    if (nx, ny) not in dist or new_dist < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_dist
                        prev[(nx, ny)] = (x, y)
                        heapq.heappush(priority_queue, (new_dist, (nx, ny)))

        execution_time = time.perf_counter() - start_time

        path = [ ]
        if start == end:
            path = [start]
        elif end in dist:
            node = end
            while node in prev:
                path.append(node)
                node = prev[node]
            path.append(start)
            path.reverse()

        return {
            "path": path,
            "distances": dist,
            "visited_order": visited_order,
            "execution_time": execution_time
        }
    
#Haciendo testing con un maze q me dio chatgpt
def main():
    maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,1,0,0],
    [0,0,0,0,0]
]

    user_input = input("Quieres ver a dijkstra jeje?: ")
        
    if user_input.capitalize() == "Yes":
        
        obj_maze = Dijkstra(maze)
        start = (0,0)
        end= (4,2)
        
        path = obj_maze.run(start,end)
        resultados = obj_maze.run_with_details(start, end)
        
        #Aqui imprimo la ruta original y tambien el resumen completo con tiempo
        print(f"La ruta mas eficiente segun el algoritmo de Dijkstra es: {path}")
        print(f"Distancia total de la ruta: {len(resultados['path']) - 1}")
        print(f"Nodos visitados en orden: {resultados['visited_order']}")
        print("Distancias minimas encontradas por nodo:")

        #Aqui muestro todos los resultados que calculo Dijkstra para cada nodo alcanzable
        for nodo, distancia in sorted(resultados["distances"].items()):
            print(f"  {nodo}: {distancia}")

        print(f"Tiempo que tardo el algoritmo: {resultados['execution_time']:.8f} segundos")
        
        
        
if __name__ == "__main__":
    main()
        
