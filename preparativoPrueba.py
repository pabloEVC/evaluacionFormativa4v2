inventario=[]
def agregarProducto(productos):
    """Esta funcion agrega los productos al diccionario"""
    disponible=False
    while True:
        nombre=input("ingrese nombre del producto: ").title()
        if nombre is any or nombre ==" ":
            print("el nombre a ingresar no debe estar vacio")
            
        else:
            break
    while True:
        try:
            
            precio=int(input("ingrese el valor de venta: $"))
            if precio > 0:
                break
            else:
                print("el valor debe ser mayor a cero")
        except ValueError:
            
            print("debe ingresar un valor numerico ")
    while True:
        try:
            stock=int(input("ingrese la cantidad de productos a ingresar: "))
            if stock>=0:
                break
            else:
                print("la cantidad a ingresar debe ser mayor a cero")
        except ValueError:
            print("debe ser valor numerico")
    productos={
        "nombre":nombre.strip(),
        "precio":int(precio),
        "stock":int(stock),
        "disponible": False
    } 

def buscarProducto(productos):
    """Esta funcion busca dentro del diccionario"""
    while True:
        if not productos:
            print("no se han ingresado productos al inventario")
            break
        else:
            nombre=input("ingrese el producto que busca: ").title()
            if nombre in productos:
                print(nombre)
                print("$",productos[nombre]["precio"])
                print("Stock",productos[nombre]["stock"])
                
                    
                break
            else:
                print("producto no encontrado")
            
            
def eliminarProducto(productos):
    
    while True:
        
        if not productos:
            print("no se han ingresado productos al inventario")
            break
        else:
            nombre=input("ingrese el nombre del producto: ").title()
            if nombre in productos:
                del productos[nombre]
                print ("producto eliminado")
            else:
                print("Producto no encontrado")

def actualizarProducto(productos):
    for producto in producto["stock"]:
        
        










opcion=0
while opcion != 6:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    while True:
        try:
            opcion=int(input("ingrese opcion: "))
            break
        except ValueError:
            print("la opcion debe ser numerico de 1 al 6")

    match opcion:
        case 1:
            agregarProducto(productos)
        case 2:
            buscarProducto(productos)
        case 3:
            eliminarProducto(productos)
        case 4:
            actualizarProducto(productos)
        case 5:
            print()
        case 6:
            print("Saliendo")
    