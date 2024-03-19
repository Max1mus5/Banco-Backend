from Models.models import Cuenta

class DB:
    def __init__(self):  
        self.cuentas = []
        self.loadFromDB()
      
    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)
        with open("bankdata.txt", "a") as file:
            file.write(f"{cuenta.num_cuenta},{cuenta.documento_id},{cuenta.nombre},{cuenta.saldo}\n")

    def mostrarCuentas(self):
      Data = []
      for cuenta in self.cuentas:
          Data.append(cuenta)
          cuenta.mostrarDatos()
          print("-" * 30)
      return Data


    def actualizarCuentas(self, num_cuenta, nuevo_saldo):
      for cuenta in self.cuentas:
        if cuenta.num_cuenta == num_cuenta:
          cuenta.saldo = nuevo_saldo
          break

      with open("bankdata.txt", "w") as file:
        for cuenta in self.cuentas:
          file.write(f"{cuenta.num_cuenta},{cuenta.documento_id},{cuenta.nombre},{cuenta.saldo}\n")


    def loadFromDB(self):
        try:
            with open("bankdata.txt", "r") as file:
                for line in file:
                    num_cuenta, documento_id, nombre, saldo = line.strip().split(',')
                    num_cuenta = int(num_cuenta)
                    documento_id = int(documento_id)
                    saldo = float(saldo)
                    self.cuentas.append(Cuenta(num_cuenta, documento_id, nombre, saldo))
        except FileNotFoundError:
            print("No se encontró la base de datos. Se creará una nueva.")
            open("bankdata.txt", "w").close()

#listado de todas las funciones con sus parametros
#agregarCuenta(cuenta)
#mostrarCuentas()
#actualizarCuentas(num_cuenta, nuevo_saldo)
#loadFromDB()
    