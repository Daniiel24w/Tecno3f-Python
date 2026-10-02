#Ejercicio 1: Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
try:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 / num2
except ZeroDivisionError: #Division por cero
    print("Error: No se puede dividir por cero.")
else:
    print(f"El resultado de la división es: {resultado}")

#Ejercicio 2: Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
try:
    numero = 10
    texto = "Hola"
    resultado = numero + texto
except TypeError: #Error de tipos
    print("Error: No se puede sumar un número con una cadena de texto (tipos incompatibles).")

#Ejercicio 3: Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
usuario = {"nombre": "Daniel", "edad": 21}

try:
    #Accedemos a una key que no existe en el diccionario
    email = usuario["email"] #Claves validas "nombre" y "edad"
except KeyError:
    print("Error: La clave consultada no existe en el diccionario.")

#Ejercicio 4: Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
archivo = "datos.txt"

try:
    # Intentamos abrir el archivo en modo lectura ('r')
    with open(archivo, "r") as a:
        contenido = a.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{archivo}' no existe. \ns Creando el archivo...")
    # Creamos el archivo en modo escritura ('w')
    with open(archivo, "w") as a:
        a.write("Este archivo fue creado automaticamente.")
    print("Archivo creado con exito.")

#Ejercicio 5: Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
try:
    # Si el usuario ingresa un texto, float() lanza ValueError
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    # Si num2 es 0, lanza ZeroDivisionError
    resultado = num1 / num2

except ValueError:
    print("Error: Ingrese un numero valido.")
except ZeroDivisionError:
    print("Error: No es posible dividir por cero.")
else:
    print(f"El resultado es: {resultado}")

