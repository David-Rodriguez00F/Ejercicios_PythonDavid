#Ejercicio 4

#Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
#comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
#vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comision
#de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
#nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.

#Nombre y sueldo total del trabajador
nombre=input("Ingrese su nombre: ")
sueldo=int(input("Ingrese su sueldo base: "))
comisisones_ventas=int(input("Ingrese el valor de ventas: "))
division=comisisones_ventas / 100
multilplicacion=division * 1.05
print(f" Su nombre es: {nombre}, el valor de su sueldo es: {sueldo}, el valor de su comision de ventas es: {comisisones_ventas} y su sueldo total es: {sueldo + multilplicacion}")
