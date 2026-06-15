def agregarProducto(productos):
    validar=False
    while True:
        nombre=input("ingrese nombre del producto: ").title()
        if not "   " in nombre:
            nombreV=True
            break
        else:
            print("el nombre a ingresar no debe estar vacio")
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
                if stock==0:
                    disponible=False
                else:
                    disponible=True
                break
            else:
                print("la cantidad a ingresar debe ser mayor a cero")
        except ValueError:
            print("debe ser valor numerico")
    productos[nombre]={"precio":precio, "stock":stock, "disponible":disponible}
def buscarProducto(productos):
    while True:
        nombre=input("ingrese el producto que busca: ").title()
        if nombre in productos:
            print(nombre)
            print("$",productos[nombre]["precio"])
            print(productos[nombre]["stock"])
            if productos[nombre]["disponible"]==True:
                print("Disponible")
            else:
                print("sin stock")
                
            break
        else:
            print("producto no encontrado")
            
            
def eliminarProducto(productos):
    while True:
        nombre=input("ingrese el nombre del producto: ").title()
        if nombre in productos[nombre]:
            del productos[nombre]
            break
        else:
            print("Producto no encontrado")


        







productos={}


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
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print("Saliendo")
    