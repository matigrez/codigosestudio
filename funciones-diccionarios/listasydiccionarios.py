
productos = {
"mouse" : [10, 15000],
"teclado" : [5, 25000],
"monitor" : [3, 180000]
}

def agregar_producto(productos):
    nombre = input("Nombre del producto:").strip()
    
    if nombre.isdigit():
        print("debe ingresar letras")
        return

    if nombre =="":
       print("El nombre no puede ser vacio")
       return
    if nombre in productos:
        print("El producto ya existe!")
        return
    
    while True:
        try: 
            stock = int(input("ingrese stock;"))
            if stock > 0:
                break
            else:
                print("el stock debe ser mayor a cero")
        except ValueError:
            print("debe ingresar un numero, vuelva a intentarlo")

    while True:
        try: 
            precio = int(input("ingrese precio $:"))
            if precio > 0:
                break
            else:
                print("el precio debe ser mayor a cero")
        except ValueError:
            print("debe ingresar un numero, vuelva a intentarlo")

    productos[nombre] = [stock,precio]
    print("productos agregados corectamente!")



def mostrar_productos(productos):
    if len(productos) == 0:
        print("no existen productos")
        return
    for nombre in productos:
        print(nombre,"-stock:",productos[nombre][0],"-precio:",productos[nombre][1])

def buscar_productos(productos):
    if len(productos) == 0:
        print("no existen productos")
        return
    
    nombre = input("nombre producto a buscar:")
    if nombre in productos:
        print("producto encontrado")
        print(f"stock:"{productos[nombre][0]})
        print(f"precio:"{productos[nombre][1]})
    else:
        print("producto inexistente")

def productos_mas_caro(productos):
    if len(productos) == 0:
        print ("no existen productos")
        return
    mayor = 0
    mayornombre =""
    for nombre in productos:
        precio = productos[nombre][1]
        if precio > mayor:
            mayor = precio
            mayornombre = nombre
    print (f"producto mas caro es {mayornombre}")
    print (f"su precio es{mayor}")

    



while True:
    print ("\n---Inventario de productos---")
    print ("1. Agregar Productos")
    print ("2. Mostrar productos")
    print ("3. buscar producto")
    print ("4. Producto mas caro")
    print ("5. Salir")
    
    while True:
        try:    
            op = int(input("Seleccione Opcion: "))
            break
        except ValueError:
            print ("[ERROR] ingrese opcion correcta.")

    if op == 1:
        agregar_producto(productos)
    elif op == 2:
        mostrar_productos(productos)
    elif op == 3:
        buscar_productos(productos)
    elif op == 4:
        productos_mas_caro(productos)
    elif op ==5:
        print("fin del programa")
        break



    


    
