#1. Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor (65+).

# edad = int(input("Ingresa tu edad: "))

# if edad < 18:
#     print("Eres menor de edad")
# elif edad >= 18 and edad < 65:
#     print("Eres mayor de edad")
# else:
#     print("Eres adulto mayor")

#2. Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo;entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto.

# estatura = float(input("Ingresa tu estatura en metros: "))

# if estatura < 1.5:
#     print("Se te considera bajo")
# elif estatura <= 1.8:
#     print("Tu estatura es media")
# else:
#     print("Eres alto")

#3. Ingresa un numero y muestra si es multiplo de 2, de 3, o de ninguno.

# num = int(input("Ingresa un numero: "))

# if num % 2 == 0 and num % 3 == 0:
#     print("Es multiplo de 2 y de 3")
# elif num % 2 == 0:
#     print("Es multiplo de 2")
# elif num % 3 == 0:
#     print("Es multiplo de 3")
# else:
#     print("No es multiplo ni de 2 ni de 3")

#4. Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

# num = input("Escribe el numero decimal: ")
# part = num.split(".")

# if len(part) == 1:
#     print("No tiene decimales")
# else:
#     decimales = part[1]
#     if len(decimales) == 1:
#         print("Tiene 1 decimal")
#     elif len(decimales) == 2:
#         print("Tiene 2 decimales")
#     else:
#         print("Tiene más de 2 decimales")


#5. Solicita un pais y muestra si está en la siguiente tupla: ("Colombia", "Perú","Argentina", "Mexico").

# paises = ("Colombia", "Peru", "Argentina", "Mexico")

# pais = input("Ingresa un pais: ")

# if pais in paises:
#     print("El pais esta en la lista")
# else:
#     print("El pais NO está en la lista")

#6. Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

# compatibilidad = {
#     "A": ["A", "AB"],
#     "B": ["B", "AB"],
#     "AB": ["AB"],
#     "O": ["A", "B", "AB", "O"]
# }

# tipo = input("Ingrese su tipo de sangre (A, B, AB, O): ")

# if tipo in compatibilidad:
#     print("Puede donar a:", compatibilidad[tipo])
# else:
#     print("El tipo de sangre no es valido")

#7. Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y
#25, templado. Más de 25, hace calor.

# temperatura = float(input("Ingresa la temperatura en °C: "))

# if temperatura < 10:
#     print("Hace frio")
# elif temperatura <= 25:
#     print("Esta templado")
# else:
    # print("Hace calor")

#8. Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos
#números y ejecuta la operación seleccionada.

# print("OPCIONES")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")

# opcion = input("Selecciona una opcion (1, 2 o 3): ")

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# if opcion == "1":
#     resultado = num1 + num2
#     print("El resultado de la suma es:", resultado)
# elif opcion == "2":
#     resultado = num1 - num2
#     print("El resultado de la resta es:", resultado)
# elif opcion == "3":
#     resultado = num1 * num2
#     print("El resultado de la multiplicacion es:", resultado)
# else:
#     print("Opcion no valida")

#9. Pide un número entre 1 y 12 y muestra el mes correspondiente usando un
#diccionario.    

# meses = {
#     1: "Enero",
#     2: "Febrero",
#     3: "Marzo",
#     4: "Abril",
#     5: "Mayo",
#     6: "Junio",
#     7: "Julio",
#     8: "Agosto",
#     9: "Septiembre",
#     10: "Octubre",
#     11: "Noviembre",
#     12: "Diciembre"
# }

# numero = int(input("Ingresa un numero entre 1 y 12: "))

# if numero in meses:
#     print("El mes correspondiente es:", meses[numero])
# else:
#     print("Numero fuera de rango")

#10. Solicita un nu mero de 4 dígitos y determina si comienza con 1, 2 o cualquier
#otro

# numero = input("Ingresa un numero de 4 digitos: ")

# if len(numero) == 4:
#     if numero[0] == "1":
#         print("El numero comienza con 1")
#     elif numero[0] == "2":
#         print("El numero comienza con 2")
#     else:
#         print("El numero comienza con otro numero")
# else:
#     print("El numero no tiene 4 digitos")

#11. Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un
#número.

# palabra = input("Escribe una palabra: ")
# primera = palabra[0]

# vocales = "aeiouAEIOU"
# numeros = "0123456789"

# if primera in vocales:
#     print("Empieza con vocal")
# elif primera in numeros:
#     print("Empieza con un numero")
# else:
#     print("Empieza con una consonante")

#12.   Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su
#precio. Si no, indica que no está disponible   

# frutas = {
#     "manzana": 2500,
#     "pera": 1800,
#     "piña": 3000
# }

# fruta = input("Ingresa el nombre de una fruta: ")

# if fruta in frutas:
#     print("El precio de la", fruta, "es:", frutas[fruta])
# else:
#     print("La fruta no está disponible")

#13. Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4,
#aprobado. Mayor a 4, excelente.

# calificacion = float(input("Ingresa tu calificación (de 0 a 5): "))

# if calificacion < 3:
#     print("Reprobado")
# elif calificacion <= 4:
#     print("Aprobado")
# elif calificacion <= 5:
#     print("Excelente")

#14. Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

# numero = int(input("Ingresa un numero: "))

# if numero % 4 == 0 and numero % 6 == 0:
#     print("Es divisible entre 4 y 6")
# elif numero % 4 == 0:
#     print("Es divisible entre 4")
# elif numero % 6 == 0:
#     print("Es divisible entre 6")
# else:
#     print("No es posible dividir entre 4 ni 6")

#15. Crea un sistema de autenticación básico. Pide usuario y clave. Usa un
#diccionario para validar.

# usuarios = {
#     "anderson": "123",
#     "maria": "abc",
#     "juan": "cl123"
# }

# usuario = input("Ingresa tu usuario: ")
# clave = input("Ingresa tu clave: ")

# if usuario in usuarios:
#     if clave == usuarios[usuario]:
#         print("¡Autenticación exitosa!")
#     else:
#         print("Contraseña incorrecta")
# else:
#     print("Usuario no registrado")

#16. Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente
#(13-17), adulto (18-64), mayor (65+)

# edad = int(input("Ingresa tu edad: "))

# if edad >= 0 and edad <= 12:
#     print("Eres un niño")
# elif edad >= 13 and edad <= 17:
#     print("Eres un adolescente")
# elif edad >= 18 and edad <= 64:
#     print("Eres un adulto")
# elif edad >= 65:
#     print("Eres un adulto mayor")

#17. Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si
#no, muestra “ciudad secundaria”.

# capitales = ("Bogota", "Lima", "Paris", "Londres")

# ciudad = input("Ingresa el nombre de una ciudad: ")

# if ciudad in capitales:
#     print("Es una capital")
# else:
#     print("Ciudad secundaria")

# 18. Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de
# descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay
# descuento.

# valor = float(input("Ingresa el valor de la compra: "))

# if valor > 200000:
#     descuento = valor * 0.15
#     total = valor - descuento
#     print("Se aplica un 15% de descuento. Total a pagar:", total)
# elif valor >= 100000:
#     descuento = valor * 0.10
#     total = valor - descuento
#     print("Se aplica un 10% de descuento. Total a pagar:", total)
# else:
#     print("No hay descuento. Total a pagar:", valor)

#19 Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa
#de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

# nom = input("Ingresa tu nombre: ")
# horas = int(input("Ingresa el numero de horas trabajadas: "))

# tarifa = 10000
# salario_b = horas * tarifa

# if horas > 40:
#     bono = salario_base * 0.20
#     salario_t = salario_b + bono
#     print("Hola", nom, "tu salario con bono es de:", salario_t)
# else:
#     print("Hola", nom, "tu salario es de:", salario_b)

#20 Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De
#50 a 79, aceptable. 80 a 100, sobresaliente.

# puntaje = int(input("Cuanto sacaste en la prueba (0 a 100): "))

# if puntaje < 50:
#     print("No te fue bien")
# elif puntaje <= 79:
#     print("pasaste por lo basico")
# else:
#     print("Te fue muy bien")

