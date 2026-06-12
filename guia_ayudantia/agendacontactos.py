contactos = {}

def pedir_opcion():
    opcion = input("\n [A] Agregar contacto  \n[B] Buscar \n[S] Salir: ").upper()
    return opcion

def buscar_numero(agenda, nombre_buscado):
    if nombre_buscado in agenda:
        return agenda[nombre_buscado]
    else:
        return"el contacto no existe en la agenda"
    
while True:
    opcion = pedir_opcion()
    if opcion == "A":
        
        nombre = input("ingresa el nombre:").strip().title()
        numero = input("ingresa el numero:").strip().title()
        
        contactos[nombre] = numero
        print (f"contacto {nombre} guardado")
        

    elif opcion =="B":
        nombre = input("buscando contacto: ").strip().title()
        resultado = buscar_numero(contactos,nombre)
        print(f"resultado:{resultado}")


    elif opcion =="C":
        print("saliendo")
        break
    else:
        print("opcion invalida")    



