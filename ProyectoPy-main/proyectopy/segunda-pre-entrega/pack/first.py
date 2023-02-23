class Cliente:
    def __init__(self, nombre, email, edad, direccion):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.direccion = direccion
        self.carro = []
        self.compras = []
        
    def agregar_al_carro(self, producto):
        self.carro.append(producto)

    def eliminar_del_carro(self, producto):
        self.carro.remove(producto)

    def ver_carro(self):
        print("Carro de compras:")
        for producto in self.carro:
            print("- ", producto)
        
    def comprar_carro(self):
        self.compras.extend(self.carro)
        self.carro.clear()