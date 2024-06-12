from collections import deque

def valida_nodo_en_grafo(grafo_lista, nodo):
    return nodo in grafo_lista[0]

def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
    grafo_dict = {nodo: [] for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo_dict[u].append(v)
        grafo_dict[v].append(u)  

    queue = deque([(nodo_ini, [nodo_ini])])
    visitados = {nodo_ini}
    
    while queue:
        actual, camino = queue.popleft()
        if actual == nodo_fin:
            return camino
        for vecino in grafo_dict[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                queue.append((vecino, camino + [vecino]))
    
    return []


def dfs_ciclo(grafo, actual, visitados, camino):
    visitados.add(actual)
    camino.append(actual)
    
    for vecino in grafo[actual]:
        if vecino not in visitados:
            if dfs_ciclo(grafo, vecino, visitados, camino):
                return True
        elif vecino == camino[0] and len(camino) > 2:
            camino.append(vecino)
            return True
    
    camino.pop()
    return False

def encuentra_ciclo(grafo_lista, nodo):
    grafo = {nodo: [] for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo[u].append(v)
        grafo[v].append(u)

    visitados = set()
    camino = []

    if dfs_ciclo(grafo, nodo, visitados, camino):
        return camino
    else:
        return []

def dfs_camino_cerrado(grafo, actual, visitados, camino):
    visitados.add(actual)
    camino.append(actual)
    
    for vecino in grafo[actual]:
        if vecino not in visitados:
            if dfs_camino_cerrado(grafo, vecino, visitados, camino):
                return True
        elif vecino == camino[0] and len(camino) > 2:
            camino.append(vecino)
            return True
    
    camino.pop()
    return False

def encuentra_camino_cerrado(grafo_lista, nodo):
    grafo = {nodo: [] for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo[u].append(v)
        grafo[v].append(u)  

    visitados = set()
    camino = []

    if dfs_camino_cerrado(grafo, nodo, visitados, camino):
        return camino
    else:
        return []

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    grafo_dict = {nodo: [] for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo_dict[u].append(v)
        grafo_dict[v].append(u)  

    queue = deque([(nodo_ini, [nodo_ini])])
    visitados = {nodo_ini}
    
    while queue:
        actual, camino = queue.popleft()
        if actual == nodo_fin:
            return camino
        for vecino in grafo_dict[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                queue.append((vecino, camino + [vecino]))
    
    return []

def encuentra_circuito(grafo_lista, nodo):
    grafo_dict = {nodo: set() for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo_dict[u].add(v)
        grafo_dict[v].add(u)

    circuito = [nodo]
    stack = [nodo]
    visitados = set()
    while stack:
        u = stack[-1]
        if grafo_dict[u]:
            v = grafo_dict[u].pop()
            grafo_dict[v].remove(u)
            if v not in visitados:
                stack.append(v)
                visitados.add(v)
        else:
            circuito.append(stack.pop())
    return circuito


def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    grafo_dict = {nodo: [] for nodo in grafo_lista[0]}
    for (u, v) in grafo_lista[1]:
        grafo_dict[u].append(v)
        grafo_dict[v].append(u)  

    queue = deque([(nodo_ini, [nodo_ini])])
    visitados = {nodo_ini}
    
    while queue:
        actual, camino = queue.popleft()
        if actual == nodo_fin:
            return camino
        for vecino in grafo_dict[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                queue.append((vecino, camino + [vecino]))
    
    return []

def determina_caminos(camino_lista):
    if not camino_lista:
        return "Camino vacío"
    
    es_ciclo = camino_lista[0] == camino_lista[-1] and len(camino_lista) > 2
    unicos = len(set(camino_lista)) == len(camino_lista) or (len(set(camino_lista)) == len(camino_lista) - 1 and es_ciclo)
    
    if es_ciclo and unicos:
        return "Ciclo"
    elif es_ciclo:
        return "Circuito"
    elif unicos:
        return "Camino simple"
    else:
        return "Recorrido"

def test_todos_los_casos():
    # Grafo de ejemplo
    grafo_ejemplo = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'E')])
    print(valida_nodo_en_grafo(grafo_ejemplo, 'A'))  # True
    print(valida_nodo_en_grafo(grafo_ejemplo, 'F'))  # False
    print(encuentra_camino(grafo_ejemplo, 'A', 'C'))  # ['A', 'B', 'C']
    print(encuentra_camino(grafo_ejemplo, 'A', 'E'))  # []

    # Grafo mas grande y conectado
    grafo_ejemplo2 = (['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'd'), ('b', 'd'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e'), ('c', 'f')])
    print(encuentra_camino_cerrado(grafo_ejemplo2, 'a'))  # ['a', 'b', 'd', 'a'] o similar
    print(encuentra_recorrido(grafo_ejemplo2, 'b', 'f'))  # ['b', 'c', 'f'] o similar
    print(encuentra_circuito(grafo_ejemplo2, 'd'))  # ['d', 'a', 'b', 'd'] o similar
    print(encuentra_camino_simple(grafo_ejemplo2, 'a', 'd'))  # ['a', 'd']
    print(encuentra_ciclo(grafo_ejemplo2, 'a'))  # ['a', 'b', 'd', 'a'] o similar

    # Determinar caminos
    print(determina_caminos(['d','a','b','d','c','e','d']))  # Circuito
    print(determina_caminos(['a', 'b', 'c', 'd', 'a']))  # Ciclo
    print(determina_caminos(['a', 'b', 'c', 'd']))  # Camino simple
    print(determina_caminos(['a', 'b', 'd', 'e', 'c', 'b']))  # Recorrido
    print(determina_caminos([]))  # Camino vacio
