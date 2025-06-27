# frutas=[]
# print(frutas)
# f1=input("ingrese la primera fruta: ")
# f2=input("ingrese la segunda fruta: ")
# f3=input("ingrese la tercera fruta: ")
# frutas.append(f1)
# frutas.append(f2)
# frutas.append(f3)
# print(frutas)
#-------------------------------------
# edades=[]

# print(edades)

# e1=int(input("ingrese la primera edad: "))
# e2=int(input("ingrese la segunda edad: "))
# e3=int(input("ingrese la tercera edad: "))

# edades.append(e1)
# edades.append(e2)
# edades.append(e3)

# print(edades)

#------------------------

# notas=[]

# print(notas)

# n1=int(input("ingrese la primera nota: "))
# n2=int(input("ingrese la segunda nota: "))
# ope=n1+n2
# ope1=ope//2

# notas.append(n1)
# notas.append(n2)

# print(notas)
# print(f"el promedio de las notas es: {ope1}")

#--------------------------------------

# productos=[]

# print(productos)

# e1=input("ingrese el primer productos: ")
# e2=input("ingrese el segundo productos: ")
# e3=input("ingrese el tercer productos: ")

# productos.append(e1)
# productos.append(e2)
# productos.append(e3)

# print(productos)

#------------------------

# precios=[]



# n1=float(input("ingrese el primer articulo: "))
# n2=float(input("ingrese el segundo articulo: "))
# n3=float(input("ingrese el tercer articulo: "))
# ope=n1+n2+n3


# precios.append(n1)
# precios.append(n2)
# precios.append(n3)

# print(precios)
# print(f"la suma total de los articulos es: {ope}")

#---------------------ejercicios6-------

# numeros=[]

# n1=int(input("ingrese la primer numero: "))
# n2=int(input("ingrese el segundo numero: "))
# n3=int(input("ingrese el tercer numero: "))
# n4=int(input("ingrese el cuarto numero: "))

# numeros.append(n3)
# numeros.append(n2)
# numeros.append(n3)
# numeros.append(n4)

# print(f"el numero mayor es{max(numeros)} y el numero menor es {min(numeros)}")

#-----ejercicio 7-----

# nombres=[]

# nom1=input("ingrese el primer nombre: ")
# nom2=input("ingrese el segundo nombre: ")

# nombres.append(nom1)
# nombres.append(nom2)

# print(nombres

# print(f"hola {nom1}, hola {nom2}")

#------------ejercicio8----

# temperatura=[]

# tem1=float(input("ingrese la primer temperatura: "))
# tem2=float(input("ingrese la segunda temperatura: "))

# ope=tem1*9/5+32
# ope2=tem2*9/5+32

# print(f"el resultado de la primera en fahrenheit es {ope} y del segundo es {ope2}")

# furtas= ["manzana","banana","naranja","banana"]
# furtas.remove("banana")
# print(furtas)

#-----append--------------------------ejercicio 1----

# num=[]
# num.append(7)
# print(num)

#--------------------ejercicio2-----

# nombres=["Ana","luis"]
# nombres.append("carlos")
# print(nombres)

#------insert----ejercicio1------

# lista=["1","2","3"]
# lista.insert(0,"99")
# print(lista)

#--------ejercicio2------

# colores=["azul","verde"]
# colores.insert(1,"rojo")
# print(colores)

#---------extend----ejercicio1---

# lista=["1","2","3"]
# lista.extend(["4","5","6"])
# print(lista)

#--------------ejercicio2-----

# letras=["a","b"]
# letras.extend(["o","k"])
# print(letras)

#------remove--ejercicio1---

# frutas=["manzana","uva","pera"]
# frutas.remove("uva")
# print(frutas)

#-------ejercicio2----

# lista=["1","2","3","2"]
# lista.remove("2")
# print(lista)

#----pop-----ejercicio1--

# lista=[1,2,3,4]
# valor=lista.pop()
# print(valor)
# print(lista)

#----ejercicio2----

# lista=["uno","dos","tres"]
# valor=lista.pop(0)
# print(valor)
# print(lista)

# #-----clear-----ejercicio1--

# lista=[1,2,3]
# lista.clear()
# print(lista)

# #----ejercicio2-----

# lista=[1,"dos",3,"cuatro"]
# lista.clear()
# print(lista)

#----------index--ejercicio1--

# lista=["manzana","pera","uva"]
# print(lista.index("pera"))

#----ejercicio2----

# numeros=[4,5,6,7]
# print(numeros.index(6))

#----count----ejercicio1---

# lista=[3,1,3,5,3]
# print(lista.count(3))

#----ejercicio2--

# lista=["a","b","a","c","b"]
# print(lista.count(a))

#-----sort--ejercicio1

# lista=[5,1,4,2,3]
# lista.sort()
# print(lista)

#-----ejercicio2

# lista=["z","a","m","b"]
# lista.sort()
# print(lista)

#----reverse---ejercicio1--

# lista=[1,2,3,4]
# lista.reverse()
# print(lista)

#----ejercicio2-----

# lista=["inicio","medio","fin"]
# lista.reverse()
# print(lista)

#--------------------ejercicio1--

# lista=[1,2,3]
# nueva=lista.copy()
# nueva.append(3)
# print(lista)
# print(nueva)

#-----ejercicio2---

# lista=["a","b","c"]
# nueva=lista.copy()
# nueva.append("d")
# print(lista)
# print(nueva)

#------actividad de listas-------

lista1=[]
lista2=[]
lista1.append(100)
lista1.append("hola mundo")
lista2.append(300)
lista2.append("hola y adios")
lista3=lista1.copy()
lista3.remove("hola mundo")
lista4=lista2.copy()
lista4.remove("hola y adios")
lista4.remove(300)
lista5=[]
lista5.extend(lista4)
lista5.extend(lista3)
print(f"lista 1 {lista1}")
print(f"lista 2 {lista2}")
print(f"lista 3 {lista3}")
print(f"lista 5 {lista4}")
print(f"lista 5 {lista5}")


