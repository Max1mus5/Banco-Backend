class Cuenta:
    def __init__(self, num_cuenta, documento_id, nombre, saldo):
        self.num_cuenta = int(str(num_cuenta).zfill(10))
        self.documento_id = int(str(documento_id).zfill(10))
        self.nombre = nombre
        self.saldo = float(saldo)

    def depositarDinero(self, cantidad):
        retencion = cantidad * 0.19
        cantidad_neta = cantidad - retencion
        self.saldo += cantidad_neta

    def retirarDinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar la operación.")

    def mostrarDatos(self):
        print(f"Número de cuenta: {self.num_cuenta}")
        print(f"Documento de Identidad: {self.documento_id}")
        print(f"Nombre del cliente: {self.nombre}")
        print(f"Saldo actual: {self.saldo}")

    def saldo(self):
        return self.saldo