#import usuario
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarnos en el sistema....")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Cual es tu email?: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("NO te has registrado correctamente")

    def login(self):
        print('\nIdentificate en el sistema.....')
        try:
            email = input("¿Cual es tu email?: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]} te has registrado en el sistema {login[5]}")
                self.proximas_acciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto intentalo mas tarde")

    def proximas_acciones(self,usuario):
        print("""
        acciones disponibles:

            -crear notas (crear)
            -eliminar notas (eliminar)
            -mostrar notas (mostrar)
            -salir (salir)

                """)
        accion = input("¿Que quieres hacer?: ")

        hazEl = notas.acciones.Acciones()

        if accion == 'salir':
            print(f"OK!! {usuario[1]} hasta luego")
            exit()

        elif accion == 'mostrar':
            hazEl.mostrar(usuario)
            self.proximas_acciones(usuario)

        elif accion == 'eliminar':
            hazEl.borrar(usuario)
            self.proximas_acciones(usuario)

        elif accion == 'crear':
            hazEl.crear(usuario)
            self.proximas_acciones(usuario)


