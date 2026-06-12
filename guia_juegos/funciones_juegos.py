
def mostrar_menu():
    print("---MENU PRINCIPAL---")
    print("1. Ver Catálogo de Tienda ")
    print("2. Agregar juegos al carrito")
    print("3. Ver mi carrito")
    print("4. Cargar fondos a la cartera")
    print("5. Pagar carrito ")
    print("6. Ver mi biblioteca")
    print("7. Salir")
def mostrar_juegos(lista_generica):
    if len(lista_generica) == 0:
        print ("No existe ningun elemento")
    else:
        for juego in lista_generica:
            print (f"juego: {juego["titulo"]} / precio: ${juego["precio"]}")



def buscar_juego(catalogo, nombre_buscado):
    for juego in catalogo:
        if juego["titulo"].lower() == nombre_buscado.lower():
            return juego
    return None
    
def calcular_total(lista_generica)