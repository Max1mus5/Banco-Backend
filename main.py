from Controller.utils import menu
from  UI.viewFunctions import viewElegirUsuario

opcion = viewElegirUsuario()
while opcion != 5:
    menu(opcion)
    opcion = viewElegirUsuario()