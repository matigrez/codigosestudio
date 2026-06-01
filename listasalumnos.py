
def agregar_alumnos(alumnos):
    nombre = input("Nombre del alumno: ")
    if nombre.isdigit ():
        print ("[ERROR]Ingrese un valor correcto")
        return
    if nombre == "":
        print ("[ERROR]Ingrese un valor correcto")







while True:
    print ("\n---Registro de alumnos---")
    print ("1. Agregar alumno")
    print ("2. Mostrar alumno")
    print ("3. ver promedios")
    print ("4. mejor alumno")
    print ("5. Cantidad de aprobados")
    print ("6. Salir")
    
    while True:
        try:    
            op = int(input("Seleccione Opcion: "))
            break
        except ValueError:
            print ("[ERROR] ingrese opcion correcta.")

    if op == 1:
        agregar_alumnos(alumnos)
        
    elif op == 2:
        mostrar_alumnos(alumnos)
    elif op == 3:
        ver_promedios(alumnos)
    elif op == 4:
        mejor_alumno(alumnos)
    elif op ==5:
        cantidad_aprovados(alumnos)
    elif op ==6:
        print("fin del programa")
        break
        