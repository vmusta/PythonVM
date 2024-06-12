def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    grados = {}
    vertices, aristas = grafo_lista
    for vertice in vertices:
        grados[vertice] = 0
    for arista in aristas:
        grados[arista[0]] += 1
        grados[arista[1]] += 1
    return grados

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    vertices, aristas = grafo_lista
    todos_vertices = set(vertices)
    vertices_conectados = set()
    for arista in aristas:
        vertices_conectados.add(arista[0])
        vertices_conectados.add(arista[1])
    vertices_aislados = todos_vertices - vertices_conectados
    return list(vertices_aislados)

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A', 'B','C'], ['D','E']]
    '''
    vertices, aristas = grafo_lista
    componentes = []
    visitados = set()

    def dfs(vertice, componente_actual):
        visitados.add(vertice)
        componente_actual.append(vertice)
        for arista in aristas:
            if vertice == arista[0]:  # solo considera los vecinos en la direccion correcta
                vecino = arista[1]
                if vecino not in visitados:
                    dfs(vecino, componente_actual)

    for vertice in vertices:
        if vertice not in visitados:
            componente_actual = []
            dfs(vertice, componente_actual)
            componentes.append(componente_actual)

    return componentes

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1

def test_todos_los_casos():
    # Test cuenta_grado
    grafo_ejemplo_1 = (['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'B')])
    print("Resultado de cuenta_grado:", cuenta_grado(grafo_ejemplo_1))  # Salida esperada: {'A': 1, 'B': 3, 'C': 2}

    # Test vertice_aislado
    grafo_ejemplo_2 = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B')])
    print("Resultado de vertice_aislado:", vertice_aislado(grafo_ejemplo_2))  # Salida esperada: ['D', 'E']

    # Test componentes_conexas y es_conexo
    grafo_ejemplo_3 = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'E')])
    print("Resultado de componentes_conexas:", componentes_conexas(grafo_ejemplo_3))  # Salida esperada: [['A', 'B', 'C'], ['D', 'E']]
    print("Resultado de es_conexo:", es_conexo(grafo_ejemplo_3))  # Salida esperada: False

    grafo_ejemplo_4 = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')])
    print("Resultado de es_conexo:", es_conexo(grafo_ejemplo_4))  # Salida esperada: True

if __name__ == "__main__":
    test_todos_los_casos()
