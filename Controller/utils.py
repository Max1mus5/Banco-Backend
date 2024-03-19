from Models.models import Cuenta
from DataBase.DB import DB
from UI.viewFunctions import viewSolicitarDatosRegistro, viewDepositarDinero, viewSaldoActual,viewRetirarDinero,viewMostrarCuentas, viewVerificar
import random
import os

def solicitarDatosRegistro():
    os.system("cls")
    print("¡Bienvenido al registro del banco!")
    db = DB()
    num_cuenta = random.randint(1000000000, 9999999999)
    num_cuentas = [cuenta.num_cuenta for cuenta in db.cuentas]
    while num_cuenta in num_cuentas:
      num_cuenta = random.randint(1000000000, 9999999999)
    data=viewSolicitarDatosRegistro(num_cuenta)
    print("¡Registro exitoso! Su primera deposito no tiene retención.")

    return crearCuenta(data['num_cuenta'], data['documento_id'], data['nombre'], data['saldo_inicial'])


def crearCuenta(num_cuenta, documento_id, nombre, saldo_inicial):
    cuenta = Cuenta(num_cuenta, documento_id, nombre, saldo_inicial)
    return cuenta

def guardarCuentaEnDB(cuenta):
    db = DB()
    db.agregarCuenta(cuenta)
    if cuenta in db.cuentas:
        return True
    else:
        return False

def actualizarCuentasEnDB(num_cuenta, saldo):
  db = DB()
  for cuenta in db.cuentas:
    if cuenta.num_cuenta == num_cuenta:
      cuenta.saldo = saldo
  db.actualizarCuentas(num_cuenta, saldo)

def depositarDinero(num_cuenta, cantidad):
  db = DB()
  for cuenta in db.cuentas:
    if cuenta.num_cuenta == num_cuenta:
      cuenta.depositarDinero(cantidad)
      actualizarCuentasEnDB(num_cuenta, cuenta.saldo)
      return cuenta.saldo
  return "Cuenta no encontrada"

def retirarDinero(num_cuenta, cantidad):
  db = DB()
  for cuenta in db.cuentas:
    if cuenta.num_cuenta == num_cuenta:
      cuenta.retirarDinero(cantidad)
      actualizarCuentasEnDB(num_cuenta, cuenta.saldo)
      return cuenta.saldo
  return "Cuenta no encontrada"

def mostrarCuentas():
  os.system("cls")
  documento_id, password = viewVerificar()
  if documento_id == 1088239515 and password == "1088239515":
      db = DB()
      cuentas = db.mostrarCuentas()
      if cuentas:
          viewMostrarCuentas(cuentas)
      else:
          print("No hay cuentas para mostrar.")
  else:
      print("No tiene permisos para ver las cuentas")

    

def elegirUsuario():
    print("¡Bienvenido al banco UTP\n¿Que desea hacer?")
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar cuentas")
    print("5. Nada solo viene a mirar")
    opcion = int(input("Ingrese el número de la opción que desea: "))
    return opcion

def menu(opcion):
    if opcion == 1:
        if guardarCuentaEnDB(solicitarDatosRegistro()):
            print("Cuenta guardada en la base de datos.")
        else:
            print("Error al guardar la cuenta.")
    elif opcion == 2:
      os.system("cls")
      print("Para depositar dinero, ingrese el número de cuenta a depositar:")
      deposito = viewDepositarDinero()
      viewSaldoActual(depositarDinero(deposito['num_cuenta'], deposito['cantidad']))
     
    elif opcion == 3:
        os.system("cls")
        retiro = viewRetirarDinero()
        viewSaldoActual(retirarDinero(retiro['num_cuenta'], retiro['cantidad']))

    elif opcion == 4:
        mostrarCuentas()
    elif opcion == 5:
        print("Gracias por visitarnos")
    else:
        print("Opción no válida")

#listado de todas las funciones con sus parametros
#solicitarDatosRegistro()
#crearCuenta(num_cuenta, documento_id, nombre, saldo_inicial)
#guardarCuentaEnDB(cuenta)
#actualizarCuentasEnDB(num_cuenta, saldo)
#depositarDinero(num_cuenta, cantidad)
#retirarDinero(num_cuenta, cantidad)
#mostrarCuentas()
#elegirUsuario()
#menu(opcion)
        