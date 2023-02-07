# 1. Qué operadores utiliza Python en los siguientes casos:
# A. División Modular
# rta: se usa la barra de porcentaje %

# B. Exponenciación
# rta: se usa el doble asterizco **

# C. División que retorne entero.
# rta: se usa el doble slahs //

# 1
# for divisionModular in range(1, 10):
#     if(divisionModular% 2 != 0):
#         print(divisionModular)
# 2
# for exponenciacion in range(1, 10):
#     if(exponenciacion** 2 != 0):
#         print(exponenciacion)
# 3
# for divisionentera in range(1, 10):
#     if(divisionentera// 2 != 0):
#         print(divisionentera)      


# 2. En la jerarquía de operadores, cuáles son los que más
# prioridad tienen cuando el intérprete de Python los evalúa?
# rta: los datos entre parentesis y la potenciacion tienen supremacia sobre los demas

# x = 5
# y = 2
# z = x + 3 * y  # El producto tiene prioridad sobre la suma


# 3. Si hay operadores de igual precedencia, en qué orden se
# ejecutan?
# A. De izquierda a derecha
# x = 5
# y = 2
# z = x + 3 - y 

# 4. Que son las expresiones regulares en Python?
# rta: . ^ $ * + ? { } [ ] \ | ( ) cada uno tiene caracteristicas que lo diferencian y las hacen unicas, para acciones determinadas.

# 5. Enumere 5 tipos de datos en Python y suministre un valor de
# ejemplo de cada uno.
# 1
#  nombre= Angel
# 2
#  edad= 17
# 3
#  promedioacademico= 4.84
# 4
#  divorciado = True
# 5
#  hobbies= ["ejercisios", "musica", "programar"]


# 6. En sus propias palabras, qué son las funciones
# preconstruidas y proporcione 2 ejemplos.
# rta: son las funciones que el interprete lo tiene por defecto y no tenemos nesecidas de asignarle todo desde cero porque tiene su funcion predefinida.

# range() Crea una lista aritmética de números según el valor pasado como argumento.
# str() Convierte un valor numérico en texto.


# 7. Cuál es la diferencia entre un condicional simple y un
# condicional compuesto?
# rta: la unica diferencia es que la cual existe una condicion la cual se cumpla o no determinara en el proceso ya sea detenerse o continuar la diferencia que separa estas dos es que la condicional compuesta alberga un codigo
# por si la condicion no se cumple, la normal simplemente no ejecuta nada si la condicion no se cumple.

# 8. Escriba un bloque cualquiera de código en Python en donde
# utilice 2 condicionales (if) anidados.


# mediante esta linea de codigo se cumplen el ejemplo de funciones compuestas y tambien los condicionales if anidados
# num1=int(input("escribe cualquier numero:"))
# num2=int(input("escribe cualquier numero:"))
# print("El valor mayor es")
# if num1>num2:
#     print(num1)
# else:
#     print(num2)

# 9. Construya un algoritmo en Python, que permita ingresar la
# información de un empleado e imprima el nombre, los
# apellidos y la antigüedad. Los datos que se deben solicitar
# son los siguientes:
# *Nombre * Teléfono *Año de ingreso a la empresa
# *Apellidos *Edad.

# nombre=str(input("escriba su nombre:"))
# apellido=str(input("escriba su apellido:"))
# telefono=int(input("escriba su numero de telefono:"))
# ingreso=int(input("cuando ingreso a la empresa?"))
# edad=int(input("escriba su edad:"))

#print("su nombre es: " + nombre, "su apellido es: "+ apellido, "su fecha de ingreso fue en la fecha: " + ingreso)



# 10. En su casa le solicitan que realice un algoritmo en Python,
# que permita calcular el valor a pagar por concepto de
# energía eléctrica. Los datos que se conocen son los
# siguientes:
# - Mes de consumo - Valor kw
# -Total kw consumido en el mes - estrato

mes_de_consumo = "1"
total_consumido = "152"
valorkw = "668"
estrato = "3"

consumo_global= total_consumido*valorkw
if estrato==1:
    descuento=total_consumido*0.6
if estrato==2:
    descuento=total_consumido*0.5
if estrato==3:
    descuento=total_consumido*0.05

valor_total= consumo_global-descuento

print("el valor del mes: "+ mes_de_consumo, "es de:"+ valor_total)


