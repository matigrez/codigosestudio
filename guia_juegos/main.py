
catalogo_steam = [
{"titulo" : "Elden Ring", "precio" : 45499},
{"titulo" : "Cyberpunk 2077", "precio" : 39999},
{"titulo" : "Stardew Valley", "precio" : 7500},
{"titulo" : "Hollow Knight", "precio" : 8300},
{"titulo" : "Sekiro: Shadows Die Twice", "precio" : 47650},
{"titulo" : "Resident Evil 4", "precio" : 27600},
{"titulo" : "Dead by Daylight", "precio" : 11994},
{"titulo" : "Clair Obscur: Expedition 33", "precio" : 39990},
{"titulo" : "Project Zomboid", "precio" : 10500},
{"titulo" : "Backrooms: Escape Together", "precio" : 5750},
{"titulo" : "Lethal Company", "precio" : 5750},
{"titulo" : "Helldivers 2", "precio" : 28000},
{"titulo" : "Red Dead Redemption 2", "precio" : 35948},
{"titulo" : "God of War", "precio" : 35000}
]
carrito_compras = []
biblioteca_juegos = []

print("Tienda steam")
nombre_usuario = input("ingresa tu nombre:").strip()
saldo = 0 

while True:
    print(f"\nNombre de usuario:{nombre_usuario} / Cartera:{saldo}")
    fn.mostrar_menu()
    opcion = input("--->").strip()

    if opcion == 1:
        fn.mostrar_juego(catalogo_steam)
    if opcion == 2:
        nombre_compra = input("juego a ingresar al carrito: ").strip()
        juego_encontrado = fn.buscar_juego(catalogo_steam,nombre_compra)

        if juego_encontrado == None:
            print("El juego no existe")
        else:
            if juego_encontrado in carrito_compras:
                print("ya esta en el carrito")
            elif juego_encontrado in biblioteca_juegos:
                print("ya lo tienes en tu biblioteca")
            else:
                carrito_compras.append(juego_encontrado)
                print(f"")
            
    if opcion == 1:
    if opcion == 1:
    if opcion == 1:
    if opcion == 1: