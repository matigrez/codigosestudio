alumnos = {}

def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if nota >= 1.0 and nota <= 7.0:
                return nota
            print (" la nota debe estar entre 1 a 7")
        except:
            print("[ERROR] Ingrese un valor cottecto ") 
def agregar_alumnos(alumnos):
    nombre = input("Nombre del alumno: ").strip() #elimina espacios en blancos
    if nombre.isdigit ():
        print ("[ERROR]Ingrese un valor correcto")
        return
    if nombre == "":
        print ("[ERROR]Ingrese un valor correcto")
    if nombre in alumnos:
        print("[ERROR]El alumno ya existe, ingrese de nuevo")
    while True:
        try:
            cantidad =int(input("cantidad de notas:"))
            break
        except ValueError:
                print("[ERROR] Ingrese un valor correcto")  

    notas = []
    for i in range(cantidad):
        nota = leer_nota(f"ingrese nota {i+1}:")
        notas.append(nota)
    
    alumnos[nombre] = notas
    print("Alumo agregado correctamente")
def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("[ERROR] Ingrese un alumno")
        return
    for nombre in alumnos:
        print(nombre,":",alumnos[nombre] )
def ver_promedios(alumnos):
    if len(alumnos) == 0:
        print("[ERROR] Ingrese un valor correcto")
        return
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre])
        print (nombre, "Promedio: ",round(promedio,1))

def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("[ERROR] Ingrese un valor correcto")
        return
    mejor_Promedio = 0
    mejoralumno = ""
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre]) 
        if promedio > mejor_Promedio:
            mejor_Promedio = promedio
            mejoralumno = nombre
    print ("El mejor alumno es :",mejoralumno)
    print ("El promedio es :",round(mejor_Promedio,1))
def cantidad_aprobados(alumnos):
    if len(alumnos) == 0:
            print("[ERROR] Ingrese un valor correcto")
            return
    aprobados = 0
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre]) 
        if promedio >= 4.0:
            aprobados = aprobados + 1
    print ("Cantidad de aprobados: ",aprobados)

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
    elif op == 5:
        cantidad_aprobados(alumnos)
    elif op == 6:
        print("fin del programa")
        break
        