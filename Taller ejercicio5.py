#Ejercicio 5

#Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
#compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
#compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
#de la compra el valor del descuento y el valor final a pagar. 

#Valor de venta
valor_compra=int(input("Ingrese wl valor del producto: "))
descuento=0.2
valor_descuento=valor_compra*descuento
print(f"El valor del producto es: {valor_compra}, el valor del descuento es: {valor_descuento} y el valor total del producto es: {valor_compra-valor_descuento}")
