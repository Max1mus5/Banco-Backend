import tkinter as tk
from Models.models import Cuenta


def viewElegirUsuario():
    root = tk.Tk()
    opcion = None

    def handle_choice(option):
        if root.winfo_exists():  # Check if the root window still exists
            root.destroy()
        return int(option)

    def create_account():
        nonlocal opcion
        opcion = handle_choice(1)

    def deposit_money():
        nonlocal opcion
        opcion = handle_choice(2)

    def withdraw_money():
        nonlocal opcion
        opcion = handle_choice(3)

    def show_accounts():
        nonlocal opcion
        opcion = handle_choice(4)

    def do_nothing():
        nonlocal opcion
        opcion = handle_choice(5)

    root.title("Banco UTP")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label = tk.Label(frame, text="¡Bienvenido al banco UTP!", justify='center')
    label.pack()

    button1 = tk.Button(frame, text="Crear cuenta", command=create_account)
    button1.pack(pady=10)

    button2 = tk.Button(frame, text="Depositar dinero", command=deposit_money)
    button2.pack(pady=10)

    button3= tk.Button(frame, text="Retirar dinero", command=withdraw_money)
    button3.pack(pady=10)

    button4 = tk.Button(frame, text="Mostrar cuentas", command=show_accounts)
    button4.pack(pady=10)

    button5 = tk.Button(frame, text="Nada. solo viene a mirar", command=do_nothing)
    button5.pack(pady=10)

    root.update_idletasks()

    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

    root.mainloop()

    if opcion is not None:
        return opcion
    else:
        return -1
    
def viewSolicitarDatosRegistro(num_cuenta):
    root = tk.Tk()
    data = {}

    def handle_submit():
        data['num_cuenta'] = num_cuenta
        data['documento_id'] = int(entry1.get())
        data['nombre'] = entry2.get()
        data['saldo_inicial'] = float(entry3.get())
        root.destroy()

    root.title("Registro Banco UTP")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label = tk.Label(frame, text="¡Bienvenido al registro del banco UTP!", justify='center')
    label.pack()

    # su cuenta es:
    label1 = tk.Label(frame, text=f"Su cuenta es: {num_cuenta}")
    label1.pack()

    label1 = tk.Label(frame, text="Ingrese su Documento de Identidad:")
    label1.pack()
    entry1 = tk.Entry(frame)
    entry1.pack()

    label2 = tk.Label(frame, text="Ingrese su nombre:")
    label2.pack()
    entry2 = tk.Entry(frame)
    entry2.pack()

    label3 = tk.Label(frame, text="Ingrese el saldo inicial de la cuenta (el primer deposito no tiene recargo):")
    label3.pack()
    entry3 = tk.Entry(frame)
    entry3.pack()

    submit_button = tk.Button(frame, text="Submit", command=handle_submit)
    submit_button.pack(pady=10)

    root.update_idletasks()

    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

    root.mainloop()

    return data


def viewDepositarDinero():
    root = tk.Tk()
    deposito={}
    def handle_submit():
        num_cuenta = int(entry_num_cuenta.get())
        cantidad = float(entry_cantidad.get())
        deposito['num_cuenta'] = int(num_cuenta)
        deposito['cantidad'] = float(cantidad)
        root.destroy()


    root.title("Depositar Dinero")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label_num_cuenta = tk.Label(frame, text="Número de cuenta:")
    label_num_cuenta.pack()
    entry_num_cuenta = tk.Entry(frame)
    entry_num_cuenta.pack()

    label_cantidad = tk.Label(frame, text="Cantidad a depositar:")
    label_cantidad.pack()
    entry_cantidad = tk.Entry(frame)
    entry_cantidad.pack()

    submit_button = tk.Button(frame, text="Submit", command=handle_submit)
    submit_button.pack(pady=10)

    root.update_idletasks()

    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

    root.mainloop()

    return deposito

def viewRetirarDinero():
    root = tk.Tk()
    retiro={}
    def handle_submit():
        num_cuenta = int(entry_num_cuenta.get())
        cantidad = float(entry_cantidad.get())
        retiro['num_cuenta'] = int(num_cuenta)
        retiro['cantidad'] = float(cantidad)
        root.destroy()


    root.title("Retirar Dinero")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label_num_cuenta = tk.Label(frame, text="Número de cuenta:")
    label_num_cuenta.pack()
    entry_num_cuenta = tk.Entry(frame)
    entry_num_cuenta.pack()

    label_cantidad = tk.Label(frame, text="Cantidad a retirar:")
    label_cantidad.pack()
    entry_cantidad = tk.Entry(frame)
    entry_cantidad.pack()

    submit_button = tk.Button(frame, text="Submit", command=handle_submit)
    submit_button.pack(pady=10)

    root.update_idletasks()

    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

    root.mainloop()

    return retiro


def viewSaldoActual(saldo):
  root = tk.Tk()

  root.title("Saldo Actual")

  frame = tk.Frame(root)
  frame.pack(expand=True)

  label = tk.Label(frame, text=f"Su saldo actual es: ${saldo}")
  label.pack()

  root.after(2000, root.destroy)  # root.destroy will be called after 2000ms = 2 seconds

  root.update_idletasks()

  width = root.winfo_reqwidth()
  height = root.winfo_reqheight()

  root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

  root.mainloop()



def viewMostrarCuentas(cuentas):
  root = tk.Tk()
  root.title("Cuentas")

  frame = tk.Frame(root)
  frame.pack(expand=True)

  canvas = tk.Canvas(frame)
  scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
  scrollable_frame = tk.Frame(canvas)

  scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
      scrollregion=canvas.bbox("all")
    )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
  canvas.configure(yscrollcommand=scrollbar.set)

  # This is the new line of code that allows scrolling with the mouse wheel
  canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

  for cuenta in cuentas:
    label = tk.Label(scrollable_frame, text=f"Número de cuenta: {cuenta.num_cuenta}")
    label.pack()

    label = tk.Label(scrollable_frame, text=f"Documento de Identidad: {cuenta.documento_id}")
    label.pack()

    label = tk.Label(scrollable_frame, text=f"Nombre del cliente: {cuenta.nombre}")
    label.pack()

    label = tk.Label(scrollable_frame, text=f"Saldo actual: {cuenta.saldo}")
    label.pack()

    label = tk.Label(scrollable_frame, text="-" * 30)
    label.pack()

  canvas.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")

  root.update_idletasks()

  width = root.winfo_reqwidth()
  height = root.winfo_reqheight()

  root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

  root.mainloop()



def viewVerificar():
  root = tk.Tk()
  documento_id = None
  password = None

  def handle_submit():
    nonlocal documento_id, password
    documento_id = int(entry_documento_id.get())
    password = entry_password.get()
    root.destroy()

  root.title("Verificar")

  frame = tk.Frame(root)
  frame.pack(expand=True)

  label_documento_id = tk.Label(frame, text="Vamos a hacer una Verificacion de Seguridad\nPor favor ingrese su Documento de Identidad:")
  label_documento_id.pack()
  entry_documento_id = tk.Entry(frame)
  entry_documento_id.pack()

  label_password = tk.Label(frame, text="Por favor ingrese su contraseña:")
  label_password.pack()
  entry_password = tk.Entry(frame, show="*")
  entry_password.pack()

  submit_button = tk.Button(frame, text="Submit", command=handle_submit)
  submit_button.pack(pady=10)

  root.update_idletasks()

  width = root.winfo_reqwidth()
  height = root.winfo_reqheight()

  root.geometry(f"{int(width * 1.5)}x{int(height * 1.5)}+{int(root.winfo_screenwidth()/2 - width/2)}+{int(root.winfo_screenheight()/2 - height/2)}")

  root.mainloop()

  return documento_id, password



#listado de todas las funciones con sus parametros
#viewElegirUsuario()
#viewSolicitarDatosRegistro(num_cuenta)
#viewDepositarDinero()
#viewRetirarDinero()
#viewSaldoActual(saldo)
#viewMostrarCuentas(cuentas)
#viewVerificar()
