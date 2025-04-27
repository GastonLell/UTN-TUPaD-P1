# Ejercicio 1
def multiplos_4():
  lista = range(4, 101, 4)
  for i in lista:
    print(i)

# Ejercicio 2
def mostrar_elementos():
  cosas_que_me_gustan = ["elemento 1", "elemento 2", "elemento 3", "elemento 4", "elemento 5"]
  print(cosas_que_me_gustan[-2])

# Ejercicio 3
def elementos_lista():
  lista_vacia = []
  lista_vacia.append("agregando")
  lista_vacia.append("palabras")
  lista_vacia.append("append")
  
  for palabra in lista_vacia:
    print(palabra)

# Ejercicio 4
def remplazar_elementos():
  animales = ["perro", "gato", "conejo", "pez"]
  animales[1] = 'loro'
  animales[-1] = 'oso'
  print(animales)

# Ejercicio 5

# crear un array con los siguientes numeros
numeros = [8, 15, 3, 27, 7]

# busca el valor maximo del array 'numeros' y elimina el elemento del array
numeros.remove(max(numeros))
# imprime la nueva lista editada
print(numeros)

# Ejercicio 6
def imprimir_primeros():
  for i in range(10, 31, 5)[0:2]:
    print(i)

# Ejercicio 7
def remplazar_autos():
  autos = ["sedan", "polo", "suran", "gol"]
  autos[1] = "Yaris"
  autos[2] = "Territory"

  print(autos)

# Ejercicio 8
def imprimir_dobles():
  dobles = []

  dobles.append(5 * 2)
  dobles.append(10 * 2)
  dobles.append(15 * 2)

  print(dobles)

# Ejercicio 9
def lista_compras():
  compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
  
  # Agregar "jugo" a la lista del tercer cliente
  compras[2].append("Jugo")

  # Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
  compras[1].remove('fideos')
  compras[1].append('tallarines')

  # Eliminar "pan" de la lista del primer cliente
  compras[0].remove('pan')

  # Imprimir la lista resultante por pantalla
  print(compras)

# Ejercicio 10
def lista_anidadas():
  lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
  ]
  print(lista_anidada)


