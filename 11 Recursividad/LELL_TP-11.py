import math;

# Ejercicio 1
def factorial_num(num):
  if num == 1:
    return 1
  else:
    return num + factorial_num(num-1)

def factorial_hasta():
  num = int(input("Ingresa un numero: "))
  for i in range(1, num + 1):
    print(f"El factorial de {i} es: {factorial_num(i)}")


# Ejercicio 2

def fibonacci_num(posicion):
  if posicion==0:
    return 0
  elif posicion==1:
    return 1
  else:
    return fibonacci_num(posicion-1) + fibonacci_num(posicion-2)

def fibonacci_hasta():
  num = int(input("Ingresa un numero: "))

  for i in range(num + 1):
    print(fibonacci_num(i))

# Ejercicio 3

def potencia_num(base, exponente):
  if exponente == 0:
    return 1
  elif exponente == 1:
    return base
  else:
    return base * potencia_num(base, exponente-1)


# Ejercicio 4

def conversor_binario(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  elif num < 0:
    convertir_numero = (num * -1)
    return f"-{str(conversor_binario(math.floor(convertir_numero / 2))) + str(convertir_numero % 2)}"
  else:
    return str(conversor_binario(math.floor(num / 2))) + str(num % 2)


# Ejercicio 5

def es_palindromo(palabra):
  palabra = palabra.lower()
  if len(palabra) == 1:
    return True
  if palabra[0] != palabra[-1]:
    return False
  
  return es_palindromo(palabra[1:-1])

# Ejercicio 6

def suma_digitos(n):
  if n < 10:
    return n
  else:
    return n % 10 + suma_digitos(n // 10)
  
# Ejercicio 7

def contar_bloques(n):
  if n == 1:
    return 1
  else:
    return n + contar_bloques(n-1)

# Ejercicio 8

def contar_digito(numero, digito):
  if numero == 0:
    return 1 if digito == 0 else 0
  else:
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

