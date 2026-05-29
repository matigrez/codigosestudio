
productos = {
"mouse" : [10, 15000],
"teclado" : [5, 25000],
"monitor" : [3, 180000]
}

def agregar_producto(productos):
    nombre = input("Nombre del producto:").strip()
    if nombre =="":
       print("El nombre no puede ser vacio")
       return
    if nombre in productos:
        print("El producto ya existe!")
        return
    stock = int(input("ingrese stock:"))
    precio = int(input("ingrese precio $:"))

    productos[nombre] = [stock,precio]
    print("productos agregados corectamente!")





while True:
    print ("\n---Inventario de productos---")
    print ("1. Agregar Productos")
    print ("2. Mostrar productos")
    print ("3. buscar producto")
    print ("4. Producto mas caro")
    print ("5. Salir")
    
    while True:
        try:    
            op = int(Input("Seleccione Opcion: "))
            break
        except ValueError:
            print ("[ERROR] ingrese opcion correcta.")
    


    
