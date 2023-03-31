print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 30 de marzo del 2023 \n")
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

valor1=numero1==numero2
#OPCION 1 
print("Los numeros "+str(numero1)+" y "+str(numero2)+ " son iguales "+str(valor1))
#OPCION 2
print("Los numeros",numero1,"y",numero2, "son iguales",valor1)
#OPCION 3
print(f"Los numeros {numero1} y {numero2} son iguales {valor1}")
#OPCION 4
print("Los numeros {} y {} son iguales {}\n".format(numero1,numero2,valor1))

valor2=numero1!=numero2
#OPCION 1 
print("Los numeros "+str(numero1)+" y "+str(numero2)+ " son distintos "+str(valor2))
#OPCION 2
print("Los numeros",numero1,"y",numero2, "son distintos",valor2)
#OPCION 3
print(f"Los numeros {numero1} y {numero2} son distintos {valor2}")
#OPCION 4
print("Los numeros {} y {} son distintos {}\n".format(numero1,numero2,valor2))

valor3=numero1>numero2
#OPCION 1 
print("Numero "+str(numero1)+" es mayor a numero " + str(numero2)+" " + str(valor3))
#OPCION 2
print("Numero",numero1,"es mayor a numero",numero2,valor3)
#OPCION 3
print(f"Numero {numero1} es mayor a numero {numero2} {valor3}")
#OPCION 4
print("Numero {} es mayor a numero {} {}\n".format(numero1,numero2,valor3))

valor4=numero1<=numero2
#OPCION 1 
print("Numero "+str(numero2)+" es mayor o igual a numero " + str(numero1)+" " + str(valor4))
#OPCION 2
print("Numero",numero2,"es mayor o igual a numero",numero1,valor4)
#OPCION 3
print(f"Numero {numero2} es mayor o igual a numero {numero1} {valor4}")
#OPCION 4
print("Numero {} es mayor o igual a numero {} {}\n".format(numero2,numero1,valor4))