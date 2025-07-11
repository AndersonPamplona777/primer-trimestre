# #1 verifica si el numero es positivo negativo o cero
# num1= float (input("ingrese un numero: "))

# if num1 > 0:
#     print("positivo")
# elif num1 < 0 : 
#     print("es negativo porque es {num1}")
# else: 
#     print (" es cero")

# #2 calcula el mayor de los numero singresados 

# num1=float(input("ingrese el primer numero: "))
# num2=float(input("ingrese el segundo numero: "))
# if num1>num2: 
#     print(f"el numero {num1} es mayor que {num2}")
# elif num2>num1: 
#     print(f"el numero {num2} es mayor que {num1}")

#3 determina si un numero es par o impar 

# num1=float(input("ingrese el numero: "))
# if num1 == 0: 
#    print ("el numero es cero que es considerado par")
# elif num1 % 2 == 0: 
#    print("el numero es par")
# else:
#     print("el numero es impar")

# # #4 dado numero verifica si esta enre 10 y 20

# num1=float(input("ingrese el numero: "))

# if 10 <= num1 <= 20:
#    print("el numero esta entre 10 y 20 ")
# else: 
#    print("el numero no esta entre 10 y 20")

#5 dados tres numeros encuentra el mayor usando condicionales 

# num1=int(input("ingrese el primer numero: "))
# num2=int(input("ingrese el segundo numero: "))
# num3=int(input("ingrese el tercer numero: "))

# if num1 >= num2 and num1 >=num3: 
#    print("el numero mayor es: ", num1)
# elif num2 >= num1 and num2 >= num3: 
#    print ("el numero mayor es: ", num2)
# else:
#    print("el numero mayor es: ", num3)

#6 calcula el precio final con un 10% de descuento si el total es mayor a $100 

# total=float(input("ingresa el total de la compra: "))
# if total > 100:
#    descuento = total * 0.10
#    total_f = total - descuento 
#    print(f"aplicaste un descuento de 10%. el precio final es: {total_f}")
# else: 
#    print(f"no aplica descuento. El precio final es: {total}")

#7 Verifica si una persona puede votar (mayor o igual a 18 años )

# edad = int(input("ingrese su edad: "))
 
# if edad >= 18: 
#    print("puedes votar.")
# else: 
#    print("no puedes votar.")


# 8. dado el precio y tipo de cliente (VIP o normal) aplica descuento del 20% solo al vip


# precio = float(input("Ingresa el precio del producto: "))
# tipo_cliente = input("Ingresa el tipo de cliente (VIP o normal): ")

# if tipo_cliente == "vip":
#     descuento = precio * 0.20
#     precio_final = precio - descuento
#     print(f"Cliente VIP. Precio con 20% de descuento: {precio_final}")
# else:
#     print(f"Cliente normal. Precio sin descuento: {precio}")

# 9 determina si un numero es multipo de 5 y de 3 al mismo tiempo

# numero = int(input("Ingresa un número: "))

# if numero % 5 == 0 and numero % 3 == 0:
#     print(f"{numero} es múltiplo de 5 y de 3.")
# else:
#     print(f"{numero} NO es múltiplo de 5 y de 3 al mismo tiempo.")

# 10 Dado un numero verifica si es divisible entre dos numeros dados  

numero = int(input("Ingresa el número: "))
d1 = int(input("Ingresa el primer divisor: "))
d2 = int(input("Ingresa el segundo divisor: "))

if numero % d1 == 0 and numero % d2 == 0:
    print("Es divisible entre los dos números")
else:
    print("No es divisible entre los dos números")




