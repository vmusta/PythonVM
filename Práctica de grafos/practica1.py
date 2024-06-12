import sys

def lee_grafo_stdin(grafo):
    vertices = grafo[1:int(grafo[0])+1]
    aristas = [(grafo[i], grafo[i+1]) for i in range(int(grafo[0])+1, len(grafo), 2)]
    return (vertices, aristas)

def lee_grafo_archivo(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    vertices = lines[1:int(lines[0])+1]
    aristas = [(lines[i], lines[i+1]) for i in range(int(lines[0])+1, len(lines), 2)]
    return (vertices, aristas)

def imprime_grafo_lista(grafo):
    return (grafo[0], grafo[1])  # devuelve una tupla con los vertices y las aristas

def lee_entrada():
    data_input = []
    n = int(input("Ingrese el número de vértices: "))
    data_input.append(str(n))
    print("Ingrese los vértices:")
    for _ in range(n):
        data_input.append(input().strip())
    m = int(input("Ingrese el número de aristas: "))
    print("Ingrese las aristas (primero el vértice origen y luego el vértice destino):")
    for _ in range(m):
        data_input.extend(list(input().strip()))
    return data_input

def main():
    grafo = lee_entrada()
    vertices, aristas = lee_grafo_stdin(grafo)
    print(imprime_grafo_lista((vertices, aristas)))

if __name__ == "__main__":
    main()
