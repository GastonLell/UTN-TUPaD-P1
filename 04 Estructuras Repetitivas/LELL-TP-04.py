from random import randint

#Actividades TP 4 Estructuras repetitivas

# Ejercicio 1:
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
def imprimir_numeros():
  for n in range(101):
    print(n)


#Ejercicio 2:
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
def cantidad_digitos():
  numero = input("Inglrese un numero entero:\n").replace("-", "")

  print(f"El numero contiene {len(numero)} digitos")


# Ejercicio 3:
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
def suma_rango():
  print("Sumaremos todos los numeros enteros comprendidos entre dos numeros\n")
  num_uno = int(input("Ingresa el primer número:\n"))
  num_dos = int(input("Ingresa el segundo número:\n"))
  suma_numeros = 0

  for i in range(num_uno+1, num_dos):
    suma_numeros += i

  print(f"La suma entre los numeros enteros comprendidos entre los numeros ingresados es: {suma_numeros}")


# Ejercicio 4:
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
def suma_numeros():
  print("Sumemos los numeros que ingreses, cuando quieras terminar la operación ingresá 0.")

  numero_ingresado = int(input("Ingrese un numero entero:\n"))
  suma_numeros = 0

  while numero_ingresado > 0:
    suma_numeros += numero_ingresado
    numero_ingresado = int(input("Ingrese un nuevo número entero (Ingrese 0 para terminar):\n"))
  print(f"La suma de los numeros ingresados es: {suma_numeros}")


# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
def adivinar_numero():
  print("Se a seleccionado un numero aleatorio entre el 0 y el 9")
  
  numero_random = randint(0,9)

  numero_ingresado = int(input("Ingresa el numero que crees que se seleccionó:"))

  intentos = 1

  while numero_ingresado != numero_random:
    intentos += 1
    numero_ingresado = int(input("Vuelve a intentarlo:"))

  print(f"Felicidades, acertasete en {intentos} intentos!")


# Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
def imprimir_pares():
  for i in range(100, 0, -2):
    print(i)


# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
def sumar_numeros_hasta():
  print("Sumaremos todos los numeros enteros comprendidos entre 0 y el numero que indiques.")
  limite = int(input("Ingrese numero positivo:\n"))

  while limite <= 0:
    limite = int(input("El numero debe ser mayor a 0:\n"))

  sumatoria = 0

  for i in range(0, limite+1):
    sumatoria += i

  print(f"La suma de todos los numeros es: {sumatoria}")


# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
def contador_tipo_numero():
  limite = 100

  print(f"Debes ingresar {limite} numeros")
  positivos = 0
  pares = 0
  cero = 0
  for i in range(0, limite):
    numero = int(input(f"Número {i+1}: "))
    if numero == 0:
      cero += 1
      continue
    
    if numero % 2 == 0:
      pares += 1

    if numero > 0:
      positivos += 1
    
  print(f"Numeros positivos: {positivos}")
  print(f"Numeros negativos: {limite - positivos - cero}")
  print(f"Numeros pares: {pares}")
  print(f"Numeros impares: {limite - pares - cero}")
  print(f"Ingresaste {cero} ceros")


# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
def media_entre_numeros():
  limite = 6
  suma = 0

  print(f"Debes ingresar {limite} numeros enteros")

  for i in range(0, limite):
    numero = int(input(f"Número {i+1}: "))
    suma += numero
  
  print(f"La media entre los numeros ingresados es: {suma / limite}")


# Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def invertir_numero():
  numero = input("Ingrese un numero para invertir su orden de digitos:\n")

  numero_invertido = ''

  for i in range(len(numero), 0, -1):
    numero_invertido += numero[i -1]

  print(f"El numero inverido es: {numero_invertido}")