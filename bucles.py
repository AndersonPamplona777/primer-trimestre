# num=int(input("ingrese un numero: "))
# while num > 0:
#     print(f"{num}")
#     num -=1
# print ("termino el conteo")


#----

# numero= int(input("ingrear numero dela tabla de multiplicar: ")) # pide al usuario un numero y lo convierte a entero 

# i = 1 # inicializamos el contador en 1 (primer multiplicador)

# print(f"\n inicia el contador en 1 {numero}: ") # imprime un titulo para la tabla de multiplicar

# while i <= 10: # bucle que se repite mientras y sea menor a o igual 10 
#     print(f"{numero} * {i} = {numero * i }") # muestra la multiplicacion y sus resultados
#     i += 1 # incrementa i en 1 en cada interacion para avanzar en la tabla 


#----

# i = 1
# while i < 6: 
#     print(i)
#     if i == 3:
#         break
#     i += 1

#---

# numero = 1 
# while True:
#     print(numero)
#     numero += 1
#     break 

#--- 

# x=5
# while True:
#     x -= 1 
#     print(x)
#     if x == 0:
#         break
# print("fin del bucle")


#------------

# chance= 1

# while chance <= 3:
#     txt = input ("escribe SI: ")
#     if txt == "SI":
#         print(" Ok, lo conseguiste en el intento", chance)
#         break
#     chance += 1
# else:
#     print("has agotado tus tres intentos")



#-----------EJERCICIO 1 BUCLES------WHILE---

# total = 0
# while True:
#     n1 = int(input("ingrese un numero para sumar(si quiere salir ingrese 0): "))
#     if n1 == 0:
#      break 
#     n2 =int(input("ingrese el segundo valor(si quiere salir ingrese 0): "))

#     total += n1 + n2

# print(f"la suma total es {total}")

# ------ejercicio2---------

# while True:
#     clave = input("Escribe la contraseña: ")
#     if clave == "python123":
#         break
# print("Contraseña correcta")


#----- ejercicio3---------------

# compras =[]

# while True:
#     producto = input ("Escribe un producto(o fin para terminar): ")
#     if producto == "fin":
#         break 
#     compras.append(producto)
# print(f"tu lista de compra es:", compras)


#--------ejercicio4-----

# pares= 0
# impares= 0
# contador=0

# while contador < 10 :
#     num= int(input ("escribe un numero: "))
#     if num % 2 == 0:
#         pares = pares + 1
#     else: 
#         impares = impares + 1
#     contador = contador + 1

# print("cantidad de pares: ", pares)
# print("cantidad de impares: ", impares)    



#---------ejercicio5----

# notas= []

# while True:
#     n1= input("escribe una nota entre o y 5 (o 'salir' para terminar): ")
#     if n1== "salir":
#         break 
#     nota = float(n1)
#     notas.append(nota)
# if len(notas) > 0:
#     promedio = sum(notas) / len(notas)
#     print("las notas que ingresaste fueron:", notas)
#     print("el promedio es:",promedio)
# else: 
#     print("no ingresaste notas")




#------ejercicio 6-----

# numero = int(input("escribe un numero para ver su tabla: "))
# i = 1
# while i <= 10 :
#      resultado = numero * i
#      print(numero,"x", i, "=", resultado)
#      i = i + 1


#---------ejercicio7-------

# secretosqui = 17
# intento = int(input("Adivina el número: "))

# while True: 
#     if intento < secretosqui:
#         print("El número es mayor")
#     elif intento > secretosqui:
#         print("El número es menor")
#     else:
#         print("¡Correcto! Adivinaste.")
#         break  
#     intento = int(input("Intenta de nuevo: "))

#------ejercicio8---------

# frutas= ("manzana", "uva", "pera", "mango", "naranja")
# adv= input("adivina una fruta: ")
# while True:
#     if adv in frutas:
#         print("¡correcto! la fruta esta en la lista")
#         break
#     else:
#         print("esa fruta no esta en la lista")
#         adv= input("intenta con otra fruta: ")



# #-----ejercicio9----

# dic= {

# "ayer": "yesterday",
# "mañana": "tomorrow",
# "hoy": " today",
# "por favor": "please",
# "hola": "hello"

# }

# palabra= input("escribe una palabra en español: ")

# while True:
#     if palabra in dic:
#         print("la traduccion de", palabra, "es:", dic[palabra])
#         break
#     else:
#         print("esta palabra no esta en el dicionario")
#         palabra = input ("intenta con otra palabra en español: ")


#------ejercicio 10------

# while True:
#     print("\n___MENU___")
#     print("1.sumar")
#     print("2.restar")
#     print("3.multiplicar")
#     print("4.dividir")
#     print("5.salir")

#     opcion= input("ingrese la opcion que desee: ")
#     if opcion == "5":
#         print("adios")
#         break
#     num1=int(input("ingrese primer numero: "))
#     num2=int(input("ingrese segundo numero: "))

#     if opcion == "1":
#         print("resultado:", num1 + num2)
#     elif opcion == "2":
#         print("resultado:", num1 - num2)
#     elif opcion == "3":
#         print("resultado", num1 * num2)
#     elif opcion == "4":
#         if num2 == 0:
#             print("no se puede dividir entre 0")
#         else:
#             print("resultado", num1 // num2)
#     else: 
#         print("opcion no valida, intentar de nuevo")


#---------ejercicio11-------


# edades= {}

# while True:
#     nombre= input ("escribe un nombre (o 'salir' para terminar): ")

#     if nombre == "salir":
#         break 

#     edad= int (input("escribe la edad:"))
#     edades[nombre] = edad 
# print("registro de edades:", edades)
