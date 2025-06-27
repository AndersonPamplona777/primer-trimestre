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

frutas = {

"manzana": "precio por kilo 3500",
"pera": "precio por kilo 4000",
"banana": "precio por kilo 2500"  
}

print(frutas)

kil=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))
kil2=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))
kil3=int(input(f"ingrese la cantidad en kilos que desea de su fruta: "))

ope=kil*3500
ope2=kil2*4000
ope3=kil3*2500

sum=ope+ope2+ope3

print(f"el total a pagar es: {sum}")





