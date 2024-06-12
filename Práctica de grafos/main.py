import sys
import importlib
import practica1
import practica2
import practica3

def ejecutar_practica1():
    importlib.reload(practica1) 
    practica1.main()

def ejecutar_practica2():
    importlib.reload(practica2)
    practica2.test_todos_los_casos()

def ejecutar_practica3():
    importlib.reload(practica3)
    practica3.test_todos_los_casos()

def main():
    while True:
        print("\nSeleccione la practica que desea ejecutar:")
        print("1. Practica 1")
        print("2. Practica 2")
        print("3. Practica 3")
        print("4. Salir")
        
        opcion = input("Ingrese el numero de la opcion: ")
        
        if opcion == '1':
            ejecutar_practica1()
        elif opcion == '2':
            ejecutar_practica2()
        elif opcion == '3':
            ejecutar_practica3()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()
