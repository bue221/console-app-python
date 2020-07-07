#Paquete usuarios
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login
""")

#variable acciones
hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == 'registro':
    hazEl.registro()
    
elif accion == 'login':
    hazEl.login()
   
