def crear_estudiante(legajo, nombre, curso):
    dic = {
        "legajo": legajo,
        "nombre": nombre,
        "curso": curso,
        "notas": []
    }
    print("--- Datos ingresados ---")
    mostrar_diccionario(dic)
    return dic
def listar_estudiantes(lista:list):
    if len(lista) == 0:
        print("No hay estudiantes")
    else:
        cont = 0
        for elem in lista:
            print("id: ", cont)
            cont += 1
            mostrar_diccionario(elem)
def listar_nombres(lista:list):
    if len(lista) == 0:
        print("No hay estudiantes")
    else:
        cont = 0
        for elem in lista:
            print("id: ", cont, " Nombre: ", elem["nombre"])
            cont += 1
def mostrar_diccionario(dic: dict):
    print("Legajo: ", dic["legajo"])
    print("Nombre: ", dic["nombre"])
    print("Curso: ", dic["curso"])
    if len(dic["notas"]) == 0:
        print("No hay notas cargadas")
    else:
        print("Notas: ")
        for elem in dic["notas"]:
            print("- ", elem)
def calcularPromedioLista(lista:list):
    suma = 0
    contador = 0
    if len(lista) > 0:
        for elem in lista:
            suma += elem
            contador += 1
        promedio = suma / contador
        return promedio
    else:
        print("No hay elementos")
        return 0
        