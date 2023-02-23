from pack.Third  import Funciones

while True:
    print("""
        ----------------------------------

        ---- Bienvenido a la tienda! ----
        
        1)- Agregar un nuevo cliente
        2)- Agregar un nuevo producto
        3)- ver lista de clientes
        4)- Ver lista de productos
        5)- Agregar un producto al carro
        6)- Eliminar un producto del carro
        7)- Ver carro de compras
        8)- Finalizar compra
        9)- Detalles del cliente 
        10)- cerrar tienda
        
        ----------------------------------
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Funciones.agregar_cliente()
    elif opcion == "2":
        Funciones.agregar_producto()
    elif opcion == "3":
        Funciones.ver_clientes()
    elif opcion == "4":
        Funciones.ver_productos()
    elif opcion == "5":
        Funciones.agregar_al_carro()
    elif opcion == "6":
        Funciones.eliminar_del_carro()
    elif opcion == "7":
        Funciones.ver_carro()
    elif opcion == "8":
        Funciones.comprar_carro()
    elif opcion == "9":
        Funciones.detalle_cliente()
    elif opcion == "10":
        Funciones.salir()