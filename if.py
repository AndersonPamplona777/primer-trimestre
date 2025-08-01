# numero=32
# if numero > 40:
#     print("el numero es >")
# else:
#     print("es <")
# print("fin")

#-------------------

# edad=int(input("ingresar edad: "))

# if edad < 0:
#     print("no cumple")
# elif edad <= 11:
#     print("< de edad")
# elif edad >= 18:
#     print("> de edad")
# elif edad >= 101:
#     print("se nos fue")
# else:
#     print("edad no existe") 

#-----vocal
# vo=input("ingrese una vocal en minuscula: ")

# if v == "a":
#     print("A")
# elif vo == "e":
#     print("E")    
# elif vo == "i":
#     print("i") 
# elif vo == "o":
#     print("O") 
# elif vo == "u":
#     print("U") 
# else:
#     print("no es una vocal minuscula")

#------------------------TALLER-----------------

# num=int(input("ingrese un numero: "))
# if num > 0 :
#     print("es positivo")
# elif num < 0 :
#     print("es negativo")
# else:
#     print("es cero")

#-------ejercicio 2----

# num1=int(input("ingrese el primer numero: "))
# num2=int(input("ingrese el segundo numero: "))
# if num1 > num2:
#     print("el mayor es", num1)
# else:
#     print("el mayor es", num2)

#-----------ejercicio3----

# num=int(input("ingrese numero: "))
# if num % 2 == 0:
#     print("es par")
# else:
#     print("es impar")

#--------ejercicio4----

# num=int(input("ingrese numero: "))
# if num >= 10 and num <=20:
#     print("esta entre 10 y 20")
# else:
#     print("no esta entre 10 y 20")

#-----ejercicio5---

# n1=int(input("ingrese primer numero:"))
# n2=int(input("ingrese segundo numero:"))
# n3=int(input("ingrese tercer numero:"))
# if n1 >= n2 and n1 >= n3:
#     print("el mayor es", n1)
# elif n2 >= n1 and n2 >= n3:
#     print("el mayor es", n2)
# else:
#     print("el mayor es", n3)

#----ejercicio6----

# total= float(input("total dela compra: "))

# if total > 100:
#     total=total * 0.9
# print(F"total a pagar:", total)

#-----ejercicio7---

# edad= int(input("ingrese su edad: "))
# if edad >= 18:
#     print("puede votar")
# else:
#     print("no puede votar")

#---ejercicio8---

# pr=float(input("ingrese precio:"))
# tp=input("tipo de cliente (VIP o normal:) ")
# if tp == "VIP":
#     pr=pr * 0.8
# print(F"total a pagar:", pr)
    
#-------ejercicio9------

# n1=int(input("ingrese numero: "))
# if n1 % 5 == 0 and % 3 == 0:
#     print("es multiplo de 5 y de 3")
# else:
#     print("no es multiplo de 5 y de 3")

# #------ejercicio10-----

# n1=int(input("numero: "))
# n2=int(input("divisor 1: "))
# n3=int(input("divisor 2:"))
# if n1 % n2 == 0 and n1 & n3 == 0:
#     print("es divisible entre los dos")
# else:
#     print("no es divisible entre los dos")

# ---------ejercicio11-----

# n = [4, 12, 9, 7, 5]
# if n[2] > 10:
#     print("Mayor a 10")
# else:
#     print("Menor o igual a 10")

# #-------ejercicio12-------

# num= [3, 5, 7, 9]
# if 7 in lis:
#     print("Está en la lista")
# else:
#     print("No está en la lista")

# #----------ejercicio13--------

# lis = [4, 6, 2, 8]
# suma = lista[0] + lista[1]
# if suma > 10:
#     print("Suma alta")
# else:
#     print("Suma baja")

# #-----ejercicio14------------
# nom = ["Ana", "Luis", "Pedro", "Marta"]
# ult = nombres[-1]
# if ult == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")

# #-----ejercicio15--------

# col = ["rojo", "azul", "verde"]
# if col[1] == "azul":
#     col[1] = "amarillo"
# print(colores)


#--------ejeercicio16--

# tupla = (5, 8, 12, 20)
# if tupla[0] < tupla[-1]:
#     print("Orden ascendente")
# else:
#     print("Orden descendente")

#------ejericio17----

# tupla = (25, 32, 28)
# if tupla[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")

# #--------ejercicio18---

# tupla = (1, 2, 3)
# lista = list(tupla)
# if lista[1] == 2:
#     lista[1] = 10
# tupla=tuple(lista)
# print(tupla)

# #---------ejercicio19------

# tupla = (4, 9)
# if tupla[1] > 5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

# #------ejercicio20--------

# tupla1 = (3, 4)
# tupla2 = (3, 5)
# if tupla1 == tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")

# #------ejercicio21---

# persona = {"nombre": "Juan", "edad": 17}
# if persona["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

# #------ejericicio22----

# persona = {"nombre": "Lucia", "edad": 20}
# if persona["edad"] > 18:
#     persona["edad"] = 21
# print(persona)

# #----ejercicio23----

# persona = {"nombre": "Carlos"}

# if "ciudad" in persona:
#     print("La clave 'ciudad' ya existe")
# else:
#     persona["ciudad"] = "Bogotá"

# print(persona)

# #-----ejercicio24----

# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")

# #------ejercicio25----

# productos = {"pan": 1200, "leche": 2000}
# if "pan" in productos:
#     print(productos["pan"])
# else:
#     print("Producto no disponible")


