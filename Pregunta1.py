# Una clase que creará la lista de adyacencia
class Graph:

	# Constructor
	def __init__(self, edges, n):

		# Una lista que va a almacenar cada relacion de cada nodo, en orden 0,1,2,3...
		
		self.adjList = [[] for _ in range(n)] #[[], [], [], [], []]

		# Agregamos cada nodo su respectiva relacion nodo 0 con [4], nodo 1 con [0,1]
		for src, dest in edges:
			self.adjList[src].append(dest)


# La función recursiva DFS, esta funcion recorre todos los nodos relacionados por el nodo origen
def DFS(graph, v, visited):

	# marcamos el primer nodo porque este si se visita a si mismo
	visited[v] = True

	# revisamos cada uno de los nodos reacionados, del nodo 0 revisamos [4], del 1 [0,1]
	# hasta que en algun punto salga visitado como verdadero
	for u in graph.adjList[v]:	

		# si aun no ha sido visitado entonces entra
		if not visited[u]:
			DFS(graph, u, visited)


# Es la funcion que envia a revision cada uno de los nodos de la lista de adyacencia
def isStronglyConnected(graph, n):

	# hacemos un for para cada uno de los nodos de la lista de adyacencia
	for i in range(n):

		# todas las relaciones de la lista de adyacencia inicialment eson marcados como no visitados
		visited = [False] * n

		# empezamos a revisar el nodo asignado para saber si visita todos los nodos y ninguno queda como falso
		DFS(graph, i, visited)

		# Si todos los nodos quedan como verdadero, al final de este for no retornará falso
		# Si en algun for este encuentra una visita falsa, entonces eso significa que el nodo no se comunica con todos
		for b in visited:
			if not b:
				return False

	return True


if __name__ == '__main__':

	# Creamos una lista de nodos, esto representa las relaciones de los nodos direccionados
	edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]

	# Declaramos el total de nodos, esto nos servirá para crear la cantidad de elementos en orden para la
	# lista de adyacencia
	n = 5

	# Enviamos los parametros [relacion de nodos y numero de nodos] para crear la lista de adyacencia
	graph = Graph(edges, n)

	# Si el nodo sale verdadero significa que si se comunica con todo y todas las visitas han quedado como verdaderos
	# Si el nodo sale falso significa que no comunica con uno o con mas nodos, entonces algunas visitas quedaron falsas
	if isStronglyConnected(graph, n):
		# si todos los nodos estan conectados significa que estan fuertemente conectados
		print(1)
	else:
		# si todos los nodos no estan conectados significa que no estan fuertemente conectados
		print(0)
