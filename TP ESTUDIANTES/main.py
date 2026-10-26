from funciones import*
lista_bd = []
def menu():
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Ingresar nota")
    print("4. Calcular promedio individual")
    print("5. Agregar una materia a estudiante")
    print("6. Mostrar materias cursadas de estudiante")
    op = int(input("Ingrese una opcion: "))
    return op
while True:
    op = menu()
    if op == 1:
        legajo = len(lista_bd) + 10000
        nombre = input("Ingrese su nombre: ")
        curso = input("Ingrese su curso: ")
        estudiante = crear_estudiante(legajo, nombre, curso)
        lista_bd.append(estudiante.copy())
    elif op == 2:
        listar_estudiantes(lista_bd)
        print(lista_bd)
    elif op == 3:
        listar_nombres(lista_bd)
        id = int(input("Ingrese el id correspondiente: "))
        nota = int(input("Ingrese la nota: "))
        lista_bd[id]["notas"].append(nota)
    elif op == 4:
        listar_nombres(lista_bd)
        id = int(input("Ingrese el id correspondiente: "))
        promedio = calcularPromedioLista(lista_bd[id]["notas"])
        print("El promedio es: ", promedio)


        