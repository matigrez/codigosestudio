def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Eliminar Tarea")
    print("3. Ver tareas ordenadas")
    print("4. Salir")
def imprimir_tareas(lista_tareas):
    if len(lista_tareas) == 0:
        print ("No hay tareas pendientes")
    else: 
        lista_tareas.sort()
        print("\n--- LISTA DE TAREAS ---")
        for tarea in lista_tareas:
            print (f"- {tarea}")



tareas= []
while True:
    mostrar_menu()
    try:
        op = int(input("Ingrese una Opcion: "))

    except ValueError:
        print("[ERROR] Ingrese una opcion correcta")
        continue
    if op == 1:
        nueva_tarea = input("Ingrese nueva tarea:")
        tareas.append(nueva_tarea)
        print(f"tarea {nueva_tarea} agregada con exito.")

    elif op == 2:
        if len(tareas) == 0:
            print("no hay tareas para eliminar.")
        else:
            tarea_eliminar = input("Ingresa el nombre de la tarea a eliminar:")
            if tarea_eliminar in tareas:
                tareas.remove(tarea_eliminar)
                print(f"tarea {tarea_eliminar} eliminada")
            else:
                print("La tarea no se encuentra en la lista.")
    elif op == 3:
        imprimir_tareas(tareas)
    elif op == 4:
        print("Fin del programa.")
        break
    else: 
        print("[ERROR] Opcion fuera de rango.")



