# persona={

# "nombre": "Juan",
# "edad": 30,
# "lugarnacimiento": "palmira",
# "telefono": 3157654343,
# "profe": "comunicadora",
# }

#----------

auto = {
"marca":"ford",
"modelo":"mustang",
"año": 2022,
"color":"morado",
"placa":"QSO-248"

}

#-------acceder a los valores---------------------

print(auto["año"])

#------modificar valores--------------------------

auto["año"]=2023

#----------añadir nuevos elementos----------------

auto["color"]= "rojo"

#----------eliminar elemntos-usando del-------------

del auto["modelo"]

#-------------usando .pop---------

auto.pop("marca")

#----------ejercicios de practica-------
#ejercicio 1

# n1=float(input("ingrese la primera nota: "))
# n2=float(input("ingrese la segunda nota: "))
# n3=float(input("ingrese la tercera nota: "))
# lista=[]
# lista.append(n1)
# lista.append(n2)
# lista.append(n3)
# sum=n1+n2+n3
# ope=sum/3
# print[lista]
# print(f"el promedio de sus notas: {ope}")

#---------ejercico 2---

# productos={

# "pan": 3000,
# "leche": 2500,
# "huevos": 3000


# }
      
# por=float(input(f"ingrese el porcentaje que desee aumentar: "))
# productos["pan"]+= productos["pan"]*(por/100)
# productos["leche"]+= productos["leche"]*(por/100)
# productos["huevos"]+= productos["huevos"]*(por/100)

# print(productos)

#-------ejercicio 3-----
# temperatura=[]

# tem1=float(input("ingrese la primera temperatura: "))
# tem2=float(input("ingrese la segunda temperatura: "))
# tem3=float(input("ingrese la tercera temperatura: "))
# tem4=float(input("ingrese la cuarta temperatura: "))
# tem5=float(input("ingrese la quinta temperatura: "))

# celsius=(tem1, tem2, tem3, tem4, tem5)
# ope1=tem1*9/5+32
# ope2=tem2*9/5+32
# ope3=tem3*9/5+32
# ope4=tem4*9/5+32
# ope5=tem5*9/5+32

# fahrenheit=(ope1, ope2, ope3, ope4, ope5)

# print("temperatura en °C: ", celsius)
# print("temperatura en °F: ", fahrenheit)

#-----ejercicio4----

# edades=[int(input("edad 1: ")), int(input("edad 2:")), int(input("edad 3:")), int(input("edad 4:")), int(input("edad 5:"))]

# promedio=sum(edades)/ len(edades)
# print(F"Mayor: {max(edades)}, Menor: {min(edades)}, promedio: {promedio}")

#-------ejercicio 5 ----------

# frutas = {

# "manzana": "precio por kilo 3500",
# "pera": "precio por kilo 4000",
# "banana": "precio por kilo 2500"  
# }

# print(frutas)

# kil=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))
# kil2=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))
# kil3=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))

# ope=kil*3500
# ope2=kil2*4000
# ope3=kil3*2500

# sum=ope+ope2+ope3

# print(f"el total a pagar es: {sum}")#frutas

#-----------6-----------------
# print("ingrese cinco numeros para formar una tupla")
# n1 = int(input("numero 1: "))
# n2 = int(input("numero 2: "))
# n3 = int(input("numero 3: "))
# n4 = int(input("numero 4: "))
# n5 = int(input("numero 5: "))

# mi_tupla = (n1,n2,n3,n4,n5)

# print("la suma de los elemntos en la tupla es:", sum(mi_tupla))

#---------7----

# inventario = []


# nombre1 = input("Nombre del producto 1: ")
# cantidad1 = int(input("Cantidad del producto 1: "))
# precio1 = float(input("Precio del producto 1: "))
# producto1 = {"nombre": nombre1, "cantidad": cantidad1, "precio": precio1}
# inventario.append(producto1)

# nombre2 = input("Nombre del producto 2: ")
# cantidad2 = int(input("Cantidad del producto 2: "))
# precio2 = float(input("Precio del producto 2: "))
# producto2 = {"nombre": nombre2, "cantidad": cantidad2, "precio": precio2}
# inventario.append(producto2)

# nombre3 = input("Nombre del producto 3: ")
# cantidad3 = int(input("Cantidad del producto 3: "))
# precio3 = float(input("Precio del producto 3: "))
# producto3 = {"nombre": nombre3, "cantidad": cantidad3, "precio": precio3}
# inventario.append(producto3)

# total = (
#     producto1["cantidad"] * producto1["precio"] +
#     producto2["cantidad"] * producto2["precio"] +
#     producto3["cantidad"] * producto3["precio"]
# )

# print("\nEl valor total del inventario es:", total)

#-----ejercicio 8-----

# precios = [100, 200, 300, 400, 500]

# descuento = float(input("Ingresa el descuento en porcentaje: "))
# descuento = descuento / 100

# precios[0] = precios[0] - precios[0] * descuento
# precios[1] = precios[1] - precios[1] * descuento
# precios[2] = precios[2] - precios[2] * descuento
# precios[3] = precios[3] - precios[3] * descuento
# precios[4] = precios[4] - precios[4] * descuento

# print("Precios con descuento:", precios)

#-----------ejercicio9------

# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))
# n4 = float(input("Nota 4: "))

# notas = (n1, n2, n3, n4)

# print("Nota más alta:", max(notas))
# print("Nota más baja:", min(notas))

#---------ejercicio10---

# conversiones = {
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01
# }


# unidad = input("Ingresa la unidad (km, m, cm): ")
# cantidad = float(input("Ingresa la cantidad: "))


# resultado = cantidad * conversiones[unidad]

# print("Equivalente en metros:", resultado)

#----ejercicio11------

# p1 = float(input("Precio 1: "))
# p2 = float(input("Precio 2: "))
# p3 = float(input("Precio 3: "))

# precios = [p1, p2, p3]

# iva1 = p1 * 1.19
# iva2 = p2 * 1.19
# iva3 = p3 * 1.19

# precios_con_iva = [iva1, iva2, iva3]

# print("Precios con IVA:", precios_con_iva)

#----ejercicio12-----

# n1 = int(input("Ingresa el primer número: "))
# n2 = int(input("Ingresa el segundo número: "))

# suma = n1 + n2
# resta = n1 - n2
# multiplicacion = n1 * n2
# division = n1 // n2


# operaciones = (suma, resta, multiplicacion, division)

# print("Resultados (suma, resta, multiplicación, división):", operaciones)

#------ejercicio13--

# nombre1 = input("Nombre 1: ")
# nota1 = float(input("Nota 1: "))

# nombre2 = input("Nombre 2: ")
# nota2 = float(input("Nota 2: "))

# nombre3 = input("Nombre 3: ")
# nota3 = float(input("Nota 3: "))

# estudiantes = {
#     nombre1: nota1,
#     nombre2: nota2,
#     nombre3: nota3
# }

# promedio = (nota1 + nota2 + nota3) / 3

# print(estudiantes)
# print("Promedio general:", promedio)

#----ejercicio14--

# s1 = float(input("Salario 1: "))
# s2 = float(input("Salario 2: "))
# s3 = float(input("Salario 3: "))
# s4 = float(input("Salario 4: "))
# s5 = float(input("Salario 5: "))


# salarios = [s1, s2, s3, s4, s5]


# a1 = s1 * 1.10
# a2 = s2 * 1.10
# a3 = s3 * 1.10
# a4 = s4 * 1.10
# a5 = s5 * 1.10

# salarios_aumento = [a1, a2, a3, a4, a5]

# print("Salarios con aumento del 10%:")
# print(salarios_aumento)

#------ejercicio15---

# producto1 = input("Nombre del producto 1: ")
# precio1 = float(input("Precio sin impuesto: "))

# producto2 = input("Nombre del producto 2: ")
# precio2 = float(input("Precio sin impuesto: "))

# producto3 = input("Nombre del producto 3: ")
# precio3 = float(input("Precio sin impuesto: "))

# productos = {
#     producto1: precio1,
#     producto2: precio2,
#     producto3: precio3
# }


# impuesto = float(input("\nPorcentaje de impuesto: "))

# precio_final1 = precio1 + (precio1 * impuesto / 100)
# precio_final2 = precio2 + (precio2 * impuesto / 100)
# precio_final3 = precio3 + (precio3 * impuesto / 100)

# print("\nPrecios con impuesto:")
# print(producto1, ":", precio_final1)
# print(producto2, ":", precio_final2)
# print(producto3, ":", precio_final3)

#--ejercicio16--

# e1 = int(input("Edad 1: "))
# e2 = int(input("Edad 2: "))
# e3 = int(input("Edad 3: "))
# e4 = int(input("Edad 4: "))
# e5 = int(input("Edad 5: "))

# mayores = (e1 >= 18) + (e2 >= 18) + (e3 >= 18) + (e4 >= 18) + (e5 >= 18)

# menores = 5 - mayores

# print("Mayores de edad:", mayores)
# print("Menores de edad:", menores)

#---ejercicio17----

# dolares = int(input("Cantidad en dólares: "))

# euro = 0.85
# peso = 4000
# yen = 110

# en_euros = dolares * euro
# en_pesos = dolares * peso
# en_yenes = dolares * yen

# conversiones = (en_euros, en_pesos, en_yenes)

# print("Conversión (euros, pesos, yenes):", conversiones)

#----ejercicio18----

# nombre1 = input("Nombre del producto 1: ")
# cantidad1 = int(input("Cantidad vendida: "))


# nombre2 = input("Nombre del producto 2: ")
# cantidad2 = int(input("Cantidad vendida: "))


# nombre3 = input("Nombre del producto 3: ")
# cantidad3 = int(input("Cantidad vendida: "))


# ventas = {
#     nombre1: cantidad1,
#     nombre2: cantidad2,
#     nombre3: cantidad3
# }

# total = cantidad1 + cantidad2 + cantidad3

# print("Ventas registradas:", ventas)
# print("Total de unidades vendidas:", total)

#------ejercicio19----


# t1 = float(input("Temperatura 1: "))
# t2 = float(input("Temperatura 2: "))
# t3 = float(input("Temperatura 3: "))
# t4 = float(input("Temperatura 4: "))
# t5 = float(input("Temperatura 5: "))
# t6 = float(input("Temperatura 6: "))
# t7 = float(input("Temperatura 7: "))
# t8 = float(input("Temperatura 8: "))
# t9 = float(input("Temperatura 9: "))
# t10 = float(input("Temperatura 10: "))


# temperaturas = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]


# a1 = t1 * (t1 > 30)
# a2 = t2 * (t2 > 30)
# a3 = t3 * (t3 > 30)
# a4 = t4 * (t4 > 30)
# a5 = t5 * (t5 > 30)
# a6 = t6 * (t6 > 30)
# a7 = t7 * (t7 > 30)
# a8 = t8 * (t8 > 30)
# a9 = t9 * (t9 > 30)
# a10 = t10 * (t10 > 30)

# b1 = t1 * (t1 < 10)
# b2 = t2 * (t2 < 10)
# b3 = t3 * (t3 < 10)
# b4 = t4 * (t4 < 10)
# b5 = t5 * (t5 < 10)
# b6 = t6 * (t6 < 10)
# b7 = t7 * (t7 < 10)
# b8 = t8 * (t8 < 10)
# b9 = t9 * (t9 < 10)
# b10 = t10 * (t10 < 10)


# mayores_30 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
# menores_10 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]


# print(f"Lista de temperaturas: {temperaturas}")
# print(f"Temperaturas mayores a 30 grados: {mayores_30}")
# print(f"Temperaturas menores a 10 grados: {menores_10}")

#-----ejercicio20---

# precios = [1000, 2500, 1500, 3000, 2000]

# print(f"Lista original: {precios}")

# precio_eliminar = int(input("Ingresa el precio que deseas eliminar: "))
# precios.remove(precio_eliminar)

# precio_agregar = int(input("Ingresa el nuevo precio que deseas agregar: "))
# precios.append(precio_agregar)

# precios.sort()

# print(f"Lista actualizada y ordenada: {precios}")












