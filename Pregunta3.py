from collections import deque


# A class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges, n):

		# Creamos una lista de adyacencia
		self.adjList = [[] for _ in range(n)]

		# Agregamos los nodos con su respectiva dirección
		for (src, dest) in edges:
			self.adjList[src].append(dest)


# La función recibe la lista de adyacencia, el nodo origen y el nodo final
def isReachable(graph, src, dest):

	# no es necesario obtener por parametro n, solo lo obtenemos con la funcion Len
	n = len(graph.adjList)

	# Inicializamos todos los descubiertos en falso
	discovered = [False] * n

	# create a queue for doing BFS
	q = deque()

	# iniciamos ccon el origen porque solo necesitamos empezar desde ahí
	discovered[src] = True

	# añadimos a la cola el nodo origen
	q.append(src)	

	# While que solo itera de uno en uno hasta que la cola se vacie completamente
	while q:

		# eliminamos el nodo almacenado en q y copiamos ese valor
		v = q.popleft()

		# si el nodo final es encontrado entonces finaliza el while
		if v == dest:
			return True

		# haremos una iteracion de nodos en caso tengamos varios nodos relacionados, de tal manera marcamos varios caminos
		for u in graph.adjList[v]:
			if not discovered[u]:
				# si el nodo relacionado aun no ha sido marcado, se marcará como verdadero
				discovered[u] = True
				#se añade a la cola para continuar con el while
				q.append(u)
	# en caso no exista un camino, la funcion finaliza con un false
	return False


if __name__ == '__main__':

	# List of graph edges as per the above diagram
	edges = [
		(0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
		(3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
	]

	# total number of nodes in the graph (labeled from 0 to 7)
	n = 8

	# build a graph from the given edges
	graph = Graph(edges, n)

	# source and destination vertex
	(src, dest) = (0, 7)

	# Si es falso, entonces significa que nunca encontró el nodo final v==dest
	if isReachable(graph, src, dest):
		print(1)
	else:
		print(0)
