# programa principal
import math

# helpers
def ingreso_entero_positivo(mensaje = "Ingrese un numero entero positivo: "):
  numero = int(input(mensaje))
  while numero < 0:
    print(f"{numero} no es válido.")
    numero = int(input("Por favor ingresa un valor mayor a 0: "))

  return numero

def ingreso_flotante_positivo(mensaje = "Ingrese un numero positivo:"):
  numero = float(input(mensaje))
  while numero < 0:
    print(f"{numero} no es válido.")
    numero = float(input("Por favor ingresa un valor mayor a 0: "))

  return numero

# Ejercicio 1
def imprimir_hola_mundo():
  print("Hola mundo")

# Ejercicio 2
def saludar_usuario(nombre_usuario):
  print(f"Hola {nombre_usuario}")

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio):
  return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
  return (radio * 2) * math.pi

def calcular_medidas_circulo():
  radio = float(input("Ingrese el radio del circulo: "))

  print(f"El area del circulo es: {calcular_area_circulo(radio)}")
  print(f"El perímetro del circulo es: {calcular_perimetro_circulo(radio)}")

# Ejercicio 5
def segundos_a_horas(segundos):
  return segundos / 3600

# Ejercicio 6

def tabla_multiplicar(numero):
  print(f"Tabla del {numero}:")
  for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
  return (f"{a} + {b} = {a+b}", f"{a} - {b} = {a-b}", f"{a} * {b} = {a*b}", f"{a} / {b} = {a/b}")

# Ejercicio 8
def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return format(imc, ".2f")

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
  return format(celsius * 9/5 + 32, ".2f")

# Ejercicio 10
def calcular_promedio(a, b, c):
  return (a + b + c) / 3

# principal
def main():
  # Ejercicio 1
  imprimir_hola_mundo()

  # Ejercicio 2
  saludar_usuario("Gaston")

  # Ejercicio 3
  informacion_personal("Gaston", "Lell", 29, "Chubut")

  # Ejercicio 4
  print("Ejercicio 4: Calular medidas de circulo: ")
  calcular_medidas_circulo()

  # Ejercicio 5
  print("Ejercicio 5: Convertir segundos a hora")
  segundos_a_convertir = ingreso_entero_positivo()
  print(f"{segundos_a_convertir} segundos es equivalente a {segundos_a_horas(segundos_a_convertir)}Hs")
  
  # Ejercicio 6
  print("Ejercicio 6: Tabla de un numero")
  numero_tabla = ingreso_entero_positivo()
  tabla_multiplicar(numero_tabla)

  # Ejercicio 7
  print("Ejercicio 7: Ingresa dos numeros para calcular las operaciones básicas")
  numero_uno = ingreso_entero_positivo()
  numero_dos = ingreso_entero_positivo()
  for i in operaciones_basicas(numero_uno, numero_dos):
    print(i)
  
  # Ejercicio 8
  print("Ejercicio 8: Calculemos indice de masa corporal")
  peso = ingreso_flotante_positivo("Ingrese peso en kilogramos: ")
  altura = ingreso_flotante_positivo("Ingrese altura en metros: ")
  print(f"Indice de masa corporal: {calcular_imc(peso, altura)}")

  # Ejercicio 9
  print("Ejercicio 9: Conversor grados celcius a grados fahrenheit")
  temperatura_celcius = float(input("Ingrese una temperatura en grados celcius: "))
  print(f"{temperatura_celcius}°C  equivalen a {celsius_a_fahrenheit(temperatura_celcius)}°F")

  # Ejercicio 10
  print("Ejercicio 10: Calcular promedio")
  numeros = []
  for i in range(3):
    numeros.append(ingreso_flotante_positivo(f"Ingrese el numero {i + 1}: "))
  print(f"El promedio de los numeros ingresados es: {calcular_promedio(*numeros)}")

main()