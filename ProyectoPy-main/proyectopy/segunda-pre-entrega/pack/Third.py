from pack.first import Cliente
from pack.Second import Producto
import json


clientes = []
productos = []

class Funciones:
    def agregar_cliente():
        nombre = input("\nIngresa el nombre del cliente: ")
        email = input("Ingresa su email: ")
        edad = input("Ingresa su edad: ")
        direccion = input("Ingresa su direccion: ")
        cliente = Cliente(nombre, email, edad, direccion)
        clientes.append(cliente)
        print(f"\n\nAgregaste el cliente - {nombre} - al sistema de forma exitosa.")

    def ver_clientes():
        print("\nAqui esta la lista de clientes: ")
        for cliente in clientes:
            print(f"\n_ {cliente.nombre} - {cliente.email}")          
            
    def agregar_producto():
        producto = input("\nIngresa el nombre del producto: ")
        tienda = input("Ingresa el nombre de la tienda: ")
        precio = input("Ingresa su precio: ")
        cantidad = input("Ingresa cuantos vas a agregar al carro: ")
        producto = Producto(producto, tienda, precio, cantidad)
        productos.append(producto)
        print(f"\nEl producto {producto} se agrego de forma exitosa!.")

    def ver_productos():
        print("\nLista de productos:\n")
        for producto in productos:
            print(f"\n_ {producto.producto}({producto.cantidad}) / {producto.tienda}")

    def agregar_al_carro():
        cliente = input("\nIngresa el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                producto = input("\nIngresa el nombre del producto: ")
                for p in productos:
                    if p.producto == producto:
                        c.agregar_al_carro(p)
                        print(f"\n\nAgregaste {producto} al carro de {cliente}")
                        return
                print("\nEl producto no ha sido encontrado.")
                return
        print("\n\nCliente no encontrado.")

    def eliminar_del_carro():
        cliente = input("\nIngresa el nombre del cliente: ")
        producto = input("Ingresa el nombre del producto a eliminar: ")
        for c in clientes:
            if c.nombre == cliente:
                for p in c.carro:
                    if p.producto == producto:
                        c.eliminar_del_carro(p)
                        print(f"\nEliminaste {producto} del carro de {cliente}.")
                        return
                print("Ese producto no se encuentra en el carro.")
                return
        print("Cliente no encontrado.")

    def ver_carro():
        cliente = input("\nIngresa el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                c.ver_carro()
                return
        print("Cliente no encontrado.")

    def comprar_carro():
        cliente = input("\nIngresa el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                confirmar = input(f"\n{c.nombre} querés confirmar la compra de los productos en tu carro? \n\n1 = SÍ / 2 = NO\n")
                if confirmar == "1":
                    print(f"\n\nCompra realizada con éxito!\nEnviaremos la factura a {c.email}\n\nMuchas gracias!")
                else:
                    print("Compra no finalizada.") 
                return
        print("Cliente no encontrado.")
        
    def detalle_cliente():
        cliente = input("\nIngrese el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                print(f"""
          -Nombre:    {c.nombre}
          -----------------------
          -Edad:      {c.edad}
          ----------------------- 
          -Dirección: {c.direccion}
          ----------------------- 
          -Email:     {c.email}
                      """)
                break    
            else:
                print("El cliente no existe.")
                

    def salir():
        print("\n\nFinalizando programa... ")
        exit()