import sys

def lee_grafo_stdin(grafo):
    try:
        num_vertices = int(grafo[0])
        vertices = grafo[1:num_vertices+1]
        aristas = []
        for i in range(num_vertices+1, len(grafo), 2):
            if i+1 < len(grafo):
                aristas.append((grafo[i], grafo[i+1]))
        return (vertices, aristas)
    except (IndexError, ValueError) as e:
        print(f"Error al procesar el grafo: {e}")
        return ([], [])

def lee_grafo_archivo(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        num_vertices = int(lines[0])
        vertices = lines[1:num_vertices+1]
        aristas = [tuple(line.split()) for line in lines[num_vertices+1:]]
        return (vertices, aristas)
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe.")
        return ([], [])
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return ([], [])

def imprime_grafo_lista(grafo):
    vertices, aristas = grafo
    print(f"Vértices: {vertices}")
    print(f"Aristas: {aristas}")

def lee_entrada_manual():
    data_input = []
    try:
        n = int(input("Ingrese el número de vértices: "))
        data_input.append(str(n))
        print("Ingrese los vértices:")
        for _ in range(n):
            data_input.append(input().strip())
        print("Ingrese las aristas (primero el vértice origen y luego el vértice destino). Deje en blanco para terminar:")
        while True:
            arista = input().strip()
            if arista == "":
                break
            origen, destino = arista.split()
            data_input.append(origen)
            data_input.append(destino)
    except ValueError as e:
        print(f"Error en la entrada: {e}")
    return data_input

def main():
    print("Seleccione una opción:")
    print("1. Ingresar grafo manualmente")
    print("2. Ingresar nombre del archivo")

    opcion = input("Ingrese su opción (1 o 2): ")

    if opcion == '1':
        grafo = lee_entrada_manual()
        vertices, aristas = lee_grafo_stdin(grafo)
    elif opcion == '2':
        file_path = input("Ingrese el nombre del archivo: ")
        vertices, aristas = lee_grafo_archivo(file_path)
    else:
        print("Opción no válida")
        return

    imprime_grafo_lista((vertices, aristas))

if __name__ == "__main__":
    main()
