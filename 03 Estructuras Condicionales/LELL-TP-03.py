# ejercicio 1
def mayor_de_edad():
  edad = int(input("Ingresa tu edad:"))
  if edad >= 18:
    print("Es mayor de edad")

# ejercicio 2
def aprobo_examen():
  nota = int(input("Ingresa la nota:"))
  print("Aprobado" if nota > 6 else "Desaprobado")

# ejercicio 3
def es_par():
  numero = int(input("Ingresa un numero par"))
  print("Ha ingresado un número par" if numero % 2 == 0 else "Por favor, ingrese un número par")

# ejercicio 4
def categoria_edad():
  edad = int(input("Ingresa tu edad:"))
  if (edad < 0):
    print("Edad inválida")
  elif (edad >= 0 and edad < 12):
    print("Eres un niño")
  elif (edad >= 12 and edad < 18):
    print("Eres un Adolescente")
  elif (edad >= 18 and edad < 30):
    print("Eres un adulto/a joven")
  else:
    print("Eres un adulto")

# ejercicio 5
def contrasenia_valida():
  contrasenia = input("Ingresa contraseña:")
  esContraseniaValida = len(contrasenia) >= 8 and len(contrasenia) <= 14
  print("Ha ingresado una contraseña correcta" if esContraseniaValida else "Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio 6
from statistics import mode, median, mean
import random

def calcular_sesgo():
  numeros_aleatorios = [random.randint(1,100) for i in range(50)]
  moda = mode(numeros_aleatorios)
  mediana = median(numeros_aleatorios)
  media = mean(numeros_aleatorios)
  print(numeros_aleatorios)
  print("moda", moda)
  print("mediana", mediana)
  print("media", mediana)
  if (media > mediana and mediana > moda):
    print("Sesgo positivo")
  elif (media < mediana and mediana < moda):
    print("Sesgo negativo")
  elif (media == mediana and mediana == moda):
    print("No hay sesgo")
  else:
    print("sin mensaje")

#efercicio 7
def agregar_signo():
  palabra_o_frase = input("Ingresa una palabra o frase: ").strip()
  
  if(
    palabra_o_frase.lower().endswith(tuple("aeiou"))
    ):
      print(f"{palabra_o_frase}!")
  else:
    print(palabra_o_frase)

#ejercicio 8
def formatear_nombre():
  nombre = input("Ingrese su nombre: ")
  print("\nElige una opción:")
  print("1. Mostrar el nombre en mayúsculas.")
  print("2. Mostrar el nombre en minúsculas.")
  print("3. Mostrar el nombre con la primera letra en mayúscula.")

  opcion = input("Ingresa el número de la opción (1, 2 o 3): ").strip()

  if opcion == "1":
    print(f"{nombre.upper()}")
  elif opcion == "2":
    print(f"{nombre.lower()}")
  elif opcion == "3":
    print(f"{nombre.title()}")
  else:
    print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

#ejercicio 9
def clasificar_terremoto():
  try:
    magnitud = float(input("Ingresa la magnitud del terremoto: "))

    if magnitud < 3:
      categoria = "Muy leve (imperceptible)"
    elif 3 <= magnitud < 4:
      categoria = "Leve (ligeramente perceptible)"
    elif 4 <= magnitud < 5:
      categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif 5 <= magnitud < 6:
      categoria = "Fuerte (puede causar daños en estructuras débiles)"
    elif 6 <= magnitud < 7:
      categoria = "Muy Fuerte (puede causar daños significativos)"
    else:
      categoria = "Extremo (puede causar graves daños a gran escala)"
      print(f"Clasificación: {categoria}")

  except ValueError:
    print("Error: Ingresa un número válido.")

#ejercicio 10

from datetime import timedelta, date

# utilizando if elif y else
def calcular_estacion():
  print("En que hemisferio te encuentras?")
  print("N: Norte - S: Sur")
  hemisferio = input("Ingresa N o S:").upper()
  mes_actual = input("Ingresa el mes actual (por ejemplo: 'Enero', 'Febrero', 'etc') : ")
  dia_actual = int(input("Ingresa el día actual: "))

  if hemisferio in ['N', 'S']:
    print("Hemisferio inválido")
    return

  if not dia_actual.isdigit() or dia_actual <= 0 or dia_actual >= 31:
    print("El día debe ser un número válido.")
    return
  
  if (mes_actual in ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']):
    print("Mes inválido.")
    return

  if hemisferio.upper() == 'N':
    print("En el hemisferio norte")
    if mes_actual.lower() == 'abril' or mes_actual.lower() == 'mayo' or (mes_actual.lower() == 'marzo' and dia_actual >= 21) or (mes_actual.lower() == 'junio' and dia_actual <= 20):
      print("Te encuentras en Primavera")
    elif mes_actual == 'julio' or mes_actual.lower() == 'agosto' or (mes_actual.lower() == 'junio' and dia_actual >= 21) or (mes_actual.lower() == 'septiembre' and dia_actual <= 20):
      print("Te encuentras en Verano")
    elif mes_actual == 'octubre' or mes_actual.lower() == 'noviembre' or (mes_actual.lower() == 'septiembre' and dia_actual >= 21) or (mes_actual.lower() == 'diciembre' and dia_actual <= 20):
      print("Te encuentras en Otoño")
    elif mes_actual.lower() == 'enero' or mes_actual.lower() == 'febrero' or (mes_actual.lower() == 'diciembre' and dia_actual >= 21) or (mes_actual.lower() == 'marzo' and dia_actual <= 20):
      print("Te encuentras en Invierno")
  elif hemisferio.upper() == 'S':
    print("Hemisferio Sur")
    if mes_actual.lower() == 'abril' or mes_actual.lower() == 'mayo' or (mes_actual.lower() == 'marzo' and dia_actual >= 21) or (mes_actual.lower() == 'junio' and dia_actual <= 20):
      print("Te encuentras en Otoño")
    elif mes_actual == 'julio' or mes_actual.lower() == 'agosto' or (mes_actual.lower() == 'junio' and dia_actual >= 21) or (mes_actual.lower() == 'septiembre' and dia_actual <= 20):
      print("Te encuentras en Invierno")
    elif mes_actual == 'octubre' or mes_actual.lower() == 'noviembre' or (mes_actual.lower() == 'septiembre' and dia_actual >= 21) or (mes_actual.lower() == 'diciembre' and dia_actual <= 20):
      print("Te encuentras en Primavera")
    elif mes_actual.lower() == 'enero' or mes_actual.lower() == 'febrero' or (mes_actual.lower() == 'diciembre' and dia_actual >= 21) or (mes_actual.lower() == 'marzo' and dia_actual <= 20):
      print("Te encuentras en Verano")



