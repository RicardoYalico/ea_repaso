# A class to represent a graph object
class Graph:
	def __init__(self, edges, n):
		# resize the list to hold `n` elements
		self.adj = [[] for _ in range(n)]

		# Agrega cada nodo relacionado a la lista de adyacencia
		for edge in edges:
			self.adj[edge[0]].append(edge[1])
		print(self.adj)


# Function to perform DFS traversal on the graph
def DFS(graph, v, discovered):

	# marcamos el primer nodo porque este si se visita a si mismo
	discovered[v] = True		

	# revisamos cada uno de los nodos reacionados, del nodo 0 revisamos [1], del 1 [2]
	# hasta que en algun punto salga descubierto como verdadero
	for u in graph.adj[v]:
		print("DFS: graph.adj["+str(v)+"]: "+str(graph.adj[v])+" graph.adj["+str(u)+"]: "+str(graph.adj[u])+" discovered: "+str(discovered[u]))
		if not discovered[u]:   # en caso discovered[u] sea falso aun sigue conociendo nuevos nodos
			DFS(graph, u, discovered)
		


def findRootVertex(graph, n):

	# todas las relaciones de la lista de adyacencia inicialmente eson marcados como no conocidos
	discovered = [False] * n

	#`v` será el ultimo nodo raiz encontrado, este va asigandose hasta el final
	v = 0
	# for para recorrer cada nodo
	for i in range(n):
		print("findRootVertex node: "+str(i)+" discovered: "+str(discovered[i]))
		# si es nodo ya está descubierto, saltamos al siguiente nodo
		if not discovered[i]:
			DFS(graph, i, discovered)
			v = i

	# todos los descrubridos son reseteados para volver a hacer la prueba de nodo raiz
	discovered[:] = [False] * n

	# Ejecutamos con el nodo raiz para marcar todos como verdaderos
	DFS(graph, v, discovered)

	# En caso exista una visita falsa, significará que no es un nodo raiz
	for i in range(n):
		if not discovered[i]:
			return -1

	# retornamos el nodo raiz
	return v


if __name__ == '__main__':

	# List of graph edges as per the above diagram
	edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]

	# total number of nodes in the graph (0 to 5)
	n = 6

	# build a directed graph from the given edges
	graph = Graph(edges, n)

	# find the root vertex in the graph
	root = findRootVertex(graph, n)

	if root != -1:
		print(root)
	else:
		print(-1)
