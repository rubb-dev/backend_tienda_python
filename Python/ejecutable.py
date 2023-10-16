class Usuarios:
    def __init__(self):
        self.nombre = ''
        self.apellido = ''
        self.usuario = ''
        self.password = ''

    def set_nombre(self,nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
        
    def set_apellido(self,apellido):
        self._apellido = apellido
    def get_apellido(self):
        return self._apellido
        
    def set_usuario(self,usuario):
        self._usuario = usuario
    def get_usuario(self):
        return self._usuario
        
    def set_password(self,password):
        self._password = password
    def get_password(self):
        return self._password
    
class Productos:
    def __init__(self):
        self.id = ''
        self.nombre = ''
        self.precio = ''

    def set_id(self,id):
        self._id = id
    def get_id(self):
        return self._id
        
    def set_nombre(self,nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
        
    def set_precio(self,precio):
        self._precio = precio
    def get_precio(self):
        return self._precio

class Facturas:
    def __init__(self):
        self.producto = ''
        self.usuario = ''
        self.precio = ''

    def set_producto(self,producto):
        self._producto = producto
    def get_producto(self):
        return self._producto
        
    def set_usuario(self,usuario):
        self._usuario = usuario
    def get_usuario(self):
        return self._usuario
        
    def set_precio(self,precio):
        self._precio = precio
    def get_precio(self):
        return self._precio

# Funciones con usuarios
def registrarse():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    usuario = input("Escribe tu usuario: ")
    Pass = input("Escribe tu contraseña: ")

    
    objuser.set_nombre(nombre)
    objuser.set_apellido(apellido)
    objuser.set_usuario(usuario)
    objuser.set_password(Pass)

    with open('usuarios.txt', 'a') as file:
        file.write(f"{objuser.get_nombre()},{objuser.get_apellido()},{objuser.get_usuario()},{objuser.get_password()}\n")
    file.close()
    
    return True


def logearse():
    usuario = input("Escribe tu nombre de usuario: ")
    password = input("Escribe tu contraseña: ")

    global opciones_programa
    global opciones_dic

    if usuario == "ruben" and password == "pijota2001":
        print("Admin")

        
        opciones_programa = """Selecciona una opción:
         1) Crear Productos
         2) Modificar productos
         3) Eliminar usuarios
         4) Sacar facturación total
         5) Sacar facturación usuario
         6) Salir
         """
    
        
        opciones_dic = {
        "1": "crear_productos()",
        "2": "modificar_productos()",
        "3": "eliminar_usuarios()",
        "4": "sacar_facturacion_total()",
        "5": "sacar_facturacion_usuario()",
        "6": "salir()",
        }

    else:
        with open("usuarios.txt", "r") as file:
            lineas = file.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[2] == usuario and datos[3] == password:

                    

                    objuser.set_nombre(datos[0])
                    objuser.set_apellido(datos[1])
                    objuser.set_usuario(datos[2])
                    objuser.set_password(datos[3])

                    print(objuser.get_nombre()+" "+objuser.get_apellido())

                    
                    opciones_programa = """Selecciona una opción:
                     1) Ver Productos
                     2) Comprar productos
                     3) Modificar datos
                     4) Salir
                     """
    
                    
                    opciones_dic = {
                    "1": "ver_productos()",
                    "2": "comprar_productos()",
                    "3": "modificar_datos()",
                    "4": "salir()",
                    }

        file.close()
    return True

def modificar_datos():

    usuarios = {}

    print("Estos son tus datos actuales:")
    print(f"{objuser.get_nombre()} {objuser.get_apellido()} {objuser.get_usuario()} {objuser.get_password()}")
    with open("usuarios.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                usuarios[str(k)] = [datos[0],datos[1],datos[2],datos[3]]
    file.close()


    for clave in usuarios.keys():
        val = usuarios[clave]
        if val[2] == objuser.get_usuario() and val[3] == objuser.get_password():
            eliminacion = clave
            break

    usuarios.pop(eliminacion)   

    nuevo_nombre = input("Introduce tu nuevo nombre: ")
    nuevo_apellido = input("Introduce tu nuevo apellido: ")
    nuevo_usuario = input("Introduce tu nuevo usuario: ")
    nuevo_password = input("Introduce tu nueva contraseña: ")

    objuser.set_nombre(nuevo_nombre)
    objuser.set_apellido(nuevo_apellido)
    objuser.set_usuario(nuevo_usuario)
    objuser.set_password(nuevo_password)

    usuarios[eliminacion] = [objuser.get_nombre(),objuser.get_apellido(),objuser.get_usuario(),objuser.get_password()]
    print("Estos son tus nuevos datos:")
    print(f"{objuser.get_nombre()} {objuser.get_apellido()} {objuser.get_usuario()} {objuser.get_password()}")
    
    
    with open("usuarios.txt", "w") as file:   
        for clave in usuarios.keys():
            valores = usuarios[clave]
            palabras = 0
            for v in valores:
                palabras += 1
                if palabras % 4 == 0:
                    file.write(v + "\n")
                else:
                    file.write(v + ",")
    return True

def eliminar_usuarios():

    usuarios = {}
    print("Este es un listado con todos los usuarios:")
    with open("usuarios.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                usuarios[str(k)] = [datos[0],datos[1],datos[2],datos[3]]
    file.close()        
    
    n = 0
    for clave in usuarios.keys():
        n +=1
        val = usuarios[clave]
        print(n , ")",val[0], ",",val[1], ",",val[2], ",",val[3] )
    
    eliminar= input("Introduce el número de la persona que deseas borrar: ")
    usuarios.pop(eliminar)

    print("Nueva lista de usuarios:")
    n = 0
    for clave in usuarios.keys():
        n +=1
        val = usuarios[clave]
        print(n , ")",val[0], ",",val[1], ",",val[2], ",",val[3] )
    
    with open("usuarios.txt", "w") as file:   
        for clave in usuarios.keys():
            valores = usuarios[clave]
            palabras = 0
            for v in valores:
                palabras += 1
                if palabras % 4 == 0:
                    file.write(v + "\n")
                else:
                    file.write(v + ",")
    file.close()
    return True


# Funciones con productos
def crear_productos():
    
    id = input("Escribe el id del producto: ")
    nombre = input("Escribe el nombre del producto: ")
    precio = input("Escribe el precio del producto: ")
    

    objproduct=Productos()
    objproduct.set_id(id)
    objproduct.set_nombre(nombre)
    objproduct.set_precio(precio)

    with open('productos.txt', 'a') as file:
        file.write(f"{objproduct.get_id()},{objproduct.get_nombre()},{objproduct.get_precio()}\n")
    file.close()
    
    return True

def modificar_productos():

    productos = {}
    print("Este es un listado con todos los productos:")
    with open("productos.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                productos[str(k)] = [datos[0],datos[1],datos[2]]
    file.close()        
    
    n = 0
    for clave in productos.keys():
        n +=1
        val = productos[clave]
        print(n , ")",val[0], ",",val[1], ",",val[2] )
    
    eliminar= input("Introduce el número del producto que deseas cambiar: ")
    productos.pop(eliminar)

  
    nuevo_id = input("Introduce el nuevo id: ")
    nuevo_nombre = input("Introduce el nuevo nombre: ")
    nuevo_precio = input("Introduce el nuevo precio: ")

    objproduct=Productos()
    objproduct.set_id(nuevo_id)
    objproduct.set_nombre(nuevo_nombre)
    objproduct.set_precio(nuevo_precio)

    productos[eliminar] = [objproduct.get_id(),objproduct.get_nombre(),objproduct.get_precio()]
    print("Estos son los nuevos datos del producto:")
    print(f"{objproduct.get_id()} {objproduct.get_nombre()} {objproduct.get_precio()}")
    
    
    with open("productos.txt", "w") as file:   
        for clave in productos.keys():
            valores = productos[clave]
            palabras = 0
            for v in valores:
                palabras += 1
                if palabras % 3 == 0:
                    file.write(v + "\n")
                else:
                    file.write(v + ",")
    return True

def ver_productos():

    productos = {}
    print("Este es un listado con todos los productos:")
    with open("productos.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                productos[str(k)] = [datos[0],datos[1],datos[2]]
    file.close()        
    
    n = 0
    for clave in productos.keys():
        n +=1
        val = productos[clave]
        print(n , ")",val[0], ",",val[1], ",",val[2] )
    
    print("""Introduce un número para seleccionar la acción:
    1) Comprar un producto: 
    2) Volver atras: 
    """)
    opcion = input()
    if opcion == "1":
        comprar_productos()
        return True
    if opcion == "2":
        return True

def comprar_productos():

    productos = {}
    print("Este es un listado con todos los productos:")
    with open("productos.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                productos[str(k)] = [datos[0],datos[1],datos[2]]
    file.close()        
    
    n = 0
    for clave in productos.keys():
        n +=1
        val = productos[clave]
        print(n , ")",val[0], ",",val[1], ",",val[2] )
    
    comprar= input("Introduce el número del producto que deseas comprar: ")
    comprado = productos[comprar]

    objfactura=Facturas()
    objfactura.set_producto(comprado[0])
    objfactura.set_usuario(objuser.get_usuario())
    objfactura.set_precio(comprado[2])
    print("GRACIAS POR SU COMPRA!!")
    print("Aquí esta su factura:")
    print(f"Producto: {objfactura.get_producto()}\nUsuario:  {objfactura.get_usuario()}\nPrecio: {objfactura.get_precio()}")
    
    with open('facturas.txt', 'a') as file:
        file.write(f"{objfactura.get_producto()},{objfactura.get_usuario()},{objfactura.get_precio()}\n")
    file.close()

    return True

# Funciones facturas
def sacar_facturacion_total():
    
    total = 0
    print("Esta es la facturación total:")
    with open("facturas.txt", "r") as file:
            lineas = file.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                total += float(datos[2])
    file.close()        
    print(total,"euros")
    return True

def sacar_facturacion_usuario():
    
    total_usuario = 0
    usuarios = {}
    print("Este es un listado con todos los usuarios:")
    with open("usuarios.txt", "r") as file:
            lineas = file.readlines()
            k = 0
            for linea in lineas:
                k += 1
                datos = linea.strip().split(",")
                usuarios[str(k)] = datos[2]
    file.close()        
    
    n = 0
    for clave in usuarios.keys():
        n +=1
        val = usuarios.get(clave)
        print(n , ")",val )
    
    user= input("Introduce el usuario del que quieres saber la facturación: ")
    dat = usuarios.get(user)

    print("Esta es la facturacion de",dat,":")
    with open("facturas.txt", "r") as file:
            lineas = file.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[1] == dat:
                    total_usuario += float(datos[2])
    file.close()        
    print(total_usuario,"euros")

    return True



def salir():
    print("Adiós")
    return False

def switch(opcion):
    diccionario = opciones_dic
    return eval(diccionario.get(opcion))


objuser = Usuarios()
continuar = True
opciones_programa = """Selecciona una opción:
          1) Registrarse
          2) Logearse
          3) Salir
          """
opciones_dic = {
        "1": "registrarse()",
        "2": "logearse()",
        "3": "salir()",
    }

while(continuar):
    print(opciones_programa)
    opcion = input()
    try:
        continuar = switch(opcion)
    except Exception as a:
        print("Selecciona una opción valida", a)


