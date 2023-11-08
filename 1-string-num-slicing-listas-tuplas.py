
'''
Dadas cuatro variables con diferentes textos, genera una nueva variable con el siguiente contenido:
“Python es un lenguaje de programación versátil”.
'''
Partiendo de:
cadena_1 = “versátil”
cadena_2 = “Python”
cadena_3 = “es un lenguaje”
cadena_4 = “de programación”

cadena_1 = 'versátil'
cadena_2 = 'Python'
cadena_3 = 'es un lenguaje'
cadena_4 = 'de programación'

frase = cadena_2 + ' ' + cadena_3 + ' ' + cadena_4 + ' ' + cadena_1
print(frase)

'''
Actividad números
En Tech Conect se va a realizar un torneo de fútbol interno de la compañía. Como parte del equipo de desarrollo, solicitan desarrollar un programa que permita calcular el promedio final de los equipos de fútbol en un torneo.
Para ello, debes considerar tres aspectos:

Jugaron 20 partidos durante el torneo.
Los partidos poseen diferente puntaje según el resultado:
Ganado: 3 puntos
Empatado: 1 punto
Perdido: 0 puntos
El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos.
Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().
'''

partidos_jugados = 20

puntaje_ganado = 3
puntaje_empatado = 1
puntaje_perdido = 0

partidos_ganados = int(input('Cuantos partidos gano tu equipo: '))
partidos_perdidos = int(input('Cuantos partidos perdio tu equipo: '))
partidos_empatados = int(input('Cuantos partidos empato tu equipo: '))

promedio = (partidos_ganados * puntaje_ganado + partidos_empatados) / partidos_jugados

print('El promedio de puntos por patido obetnidos fue', promedio)

'''
Slicing
Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.
De forma individual, realiza lo siguiente:

Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1].
Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
Extraer la nota y almacenarla en una variable llamada nota.
Extraer la materia y almacenarla en una variable llamada materia.
Mostrar por pantalla la siguiente estructura "NOMBRE APELLIDO ha sacado un NOTA en MATERIA"
Esto ultimo hacerlo, formateando las anteriores variables en una variable llamada cadena_formateada
cadena = “acitametaM ,5.8 ,otipeP ordeP”

Para formatear ¡recuerda concatenar!
'''
cadena = "acitametaM ,5.8 ,otipeP ordeP"
# 1
cadena_volteada = cadena[::-1]
print(cadena_volteada)
# 2
nombre_alumno = cadena_volteada[:12]
print(nombre_alumno)
# 3
nota = cadena_volteada[14:17]
print(nota)
# 4
materia = cadena_volteada[19:]
print(materia)
# 5
cadena_formateada = nombre_alumno + ' ha sacado un ' + {nota} + ' en ' + {materia}
print(cadena_formateada)

'''
Desafío de Listas
Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3
'''


lista1 = [1, 2, 3, 4, 'prueba', 'hola']
lista2 = [1, 5, ('mi', 'gato'), 'richard']

lista1.append(456789)
lista1.append('Hola Mundo')
print(lista1)

lista2 = lista2 + ['Hola y Adios', 5555]
print(lista2)

lista3 = lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4 + lista3
print(lista5)


# Listas 

mi_lista =  [-11,     20   ,   3,   41]
otra_lista = ['Hola', 'como', 'estas', '?']

mi_lista =  [-11, 20, 'prueba', ,3, 41]
otra_lista = ['Hola', 5, 'como', 'estas', '?', 2, 1]

datos = [1, -5, 123 ,    34, 'Una cadena', 'Otra cadena', 'Pepito’]
print(datos[0])
print(datos[-1])
print(datos[-2:])

datos = [1, -5, 123,34, ‘Una cadena’, ‘Otra cadena’]
print(datos + [0, ‘Otra cadena distinta’, ‘Pepito’, -873758,123])
numeros = [1,2,3,4]
print(numeros + [5,6,7,8])

pares =  [0,2,4,5,8,10]
pares[3] = 6
print(pares)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3] = ['A', 'B', 'C']
print(letras)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3] = []
print(letras)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras = []
print(letras)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras.clear()
print(letras)

numeros =  [1,2,3,4]
numeros.append(5)
print(numeros)

numeros =  [1,2,3,4]
numeros.append(3*2)
print(numeros)
numeros.append(3**2+1-12+5*3)
print(numeros)

numeros =  [1,2,3,4]
print(len(numeros))

datos = [1, -5, 123,34, 'Una cadena', 'Otra cadena']
print(len(datos))

numeros =  [1,2,3,4]
dato_extraido = numeros.pop()
print(numeros)
print(dato_extraido)

datos = [1, -5, 123,34, ‘Una cadena’, ‘Otra cadena’]
dato_extraido = datos .pop()
print(datos )
print(dato_extraido)

numeros = [1,2,1,3,4,1]
dato_extraido = numeros.pop(1)
print(numeros)
print(dato_extraido)

numeros =  [1,2,1,3,1,4,1]
print(numeros.count(1))

numeros = [1,2,1,3,1,4,1,5]
print(numeros.index(1))

numeros = [1,2,1,3,1,4,1,5]
print(numeros.index(7))
'''
Desafío de tuplas
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

El último ítem de tupla
El número de ítems de tupla
La posición donde se encuentra el ítem 87 de tupla
Una variable que contenga una lista con los últimos tres ítems de tupla y agregarle el 240
Un ítem que haya en la posición 8 de tupla
El número de veces que el ítem 7 aparece en tupla
Copia esta tupla para iniciar el ejercicio:
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
'''

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# 1
print(tupla[-1])

# 2
print(len(tupla))

# 3
print(tupla.index(87))

# 4
lista = list(tupla[-3:])
lista.append(240)
print(lista)

# 5
print(tupla[8])

# 6
print(tupla.count(7))





# Tuplas

mi_tupla = (1,2,3,4)
otra_tupla = ('Hola', 'como', 'estas', '?')

tupla =  (2,)
print(tupla)
tupla =  (2)
print(tupla)

mi_var = 'Una variable'
datos = (1, -5, 123,34, 'Una cadena', 'Otra cadena', mi_var)

datos = (1, -5, 123,34, 'Una cadena', 'Otra cadena')
print(datos + (0, 'Otra cadena distinta', 'Pepito', -873758,123))

numeros = (1,2,3,4)
print(numeros + (5,6,7,8))

mi_tupla = (1,2,3,4)
mi_tupla[2] = 5

letras = ('a', 'b', 'c', 'd', 'e', 'f')
letras = ()
print(letras)

datos = [155, [2,3,4], 'Una cadena', 'Otra cadena']
otros_datos = (2, (5,7,8), 1, 8)
lista_con_tupla = [1, (2,3,4), 'Una cadena', 'Otra cadena']
tupla_con_lista = (2, [5,7,8], 1, 8)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
resultado = [ a  ,b   ,   c]
print(resultado[0])
print(resultado[0][1])

numeros =  (1,2,3,4)
print(list(numeros))
datos = [1, -5, 123,34, 'Una cadena', 'Otra cadena']
print(tuple(datos))

