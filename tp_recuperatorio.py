
from funciones_tp_recuperatorio import *
from constantes import *
import random

"""
Una competencia de cocina califica a los mejores cocineros de la ciudad.
Se requieren los siguientes datos:

-Número de participante (Autoincremental) -> No se pide por input, se genera
automáticamente y se guarda en la matriz, arranca del 1 en adelante.
-Voto jurado 1 (1 al 100)
-Voto jurado 2 (1 al 100)
-Voto jurado 3 (1 al 100)

De los 5 participantes que se postularon se requiere lo siguiente:

1. Cargar Notas: Se realiza una carga secuencial de todos las notas de cada uno de los
jurados (Debe ser una matriz)
NOTA: Las notas son del 1 al 100

2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
Participante, Nota jurado 1, Nota Jurado 2, Nota jurado 3, Nota promedio

3. Ordenar votos por nota promedio: Se le pide al usuario que ingrese un orden (asc o
desc) y ordena la matriz por nota promedio.

4. Peores 3: Mostrar los peores 3 participantes en base a su nota promedio

5. Mayores promedio: Del promedio total de notas, mostrar a los participantes que
superan esa nota (siempre tomando la nota promedio)

6. Jurado malo: Mostrar cuál fue el jurado/jurados que puso en promedio las peores
notas

7. Sumatoria: Pedir un número por input (entre 3 y 300) , mostrar los participantes en los
que la suma de sus tres notas de ese número. En caso de que no haya ninguno
mostrar un mensaje de error

8. Definir ganador: Muestra al ganador de la competencia en base a su nota promedio,
en caso de haber más de uno, se realiza un desempate entre todos los ganadores.
En qué consiste el desempate: Cada uno de los jurados debe elegir el número del
participante que desea que gane, el participante más elegido gana, en caso de no
haber acuerdo (por ejemplo hay 3 participantes que ganaron y cada jurado elige a uno
distinto) el ganador se proclama de manera aleatoria.
"""

#Matriz con los participantes
participantes = inicializar_matriz(5,5,0)

#Ciclo
while(True):
    menu = menuu()
    #Menu
    match menu:      
        case 1:
            #Cargar notas
            cargar_votos(participantes)
        case 2:
            #Mostrar votos
            mostrar_votos(participantes)
        case 3:
            #Ordenar votos por nota promedio. La persona elige si quiere que sea ascendente o descendente
            opcion = input("Desea ordenarlo de manera ascendente o descendente? ")
            ordenar_votos(participantes,opcion) 
        case 4:
            #Peores 3: Mostrar los peores 3 participantes en base a su nota promedio
            print(peores_tres(participantes))          
        case 5:        
            #Mayores promedio: Del promedio total de notas, mostrar a los participantes que superan esa nota 
            mostrar_votos(mayores_promedios((participantes)))         
        case 6:
            #Mostrar cuál fue el jurado/jurados que puso en promedio las peores notas
            jurado_mlo = (jurado_malo(participantes))
            print(f"El jurado con el menor promedio es el jurado: {jurado_mlo[0]} con un valor de: {jurado_mlo[1]}")       
        case 7:  
            #Pedir un número por input (entre 3 y 300) , mostrar los participantes en los que la suma de sus tres notas de ese número    
            numero_objetivo = validar_votos("Ingrese un número entre 3 y 300: ","Error/debe ser entre 3 y 300",3,300)
            numero_objetivo = int(numero_objetivo)
            resultado = sumar_notas(participantes,numero_objetivo)
            if resultado == "No hay coincidencia":
                print("No hay coincidencia")
            else:
                print("Hubo coincidencias! ")
                mostrar_votos(resultado)               
        case 8:            
            #Muestra al ganador de la competencia en base a su nota promedio, en caso de haber más de uno,
            #se realiza un desempate entre todos los ganadores.
            #En qué consiste el desempate: Cada uno de los jurados debe elegir el número del
            #participante que desea que gane, el participante más elegido gana

            contador = 0
            mayor_promedios = (mayor_promedio(participantes))
            if len(mayor_promedios) == 1:
                print(f"El ganador es el participante: {mayor_promedios}")
                mostrar_lista(mayor_promedios)
            else:
                 # Mostrar los participantes con los mayores promedios
                mostrar_votos(mayor_promedios)
    
                # Pedir las elecciones a los jurados
                eleccion_jurado_uno = int(input("Ingrese el participante que desea que gane el jurado 1: "))
                eleccion_jurado_dos = int(input("Ingrese el participante que desea que gane el jurado 2: "))
                eleccion_jurado_tres = int(input("Ingrese el participante que desea que gane el jurado 3: "))
    
                # Guardar las elecciones en una lista para encontrar el más votado
                elecciones = {eleccion_jurado_uno, eleccion_jurado_dos, eleccion_jurado_tres}
    
                # Si todos los jurados eligen al mismo participante, ese es el ganador
                if len(elecciones) == 1:
                    ganador = eleccion_jurado_uno
                # Si hay más de una elección, hacer una votación
                elif len(elecciones) == 2:
                    # Si hay dos votos para un participante, ese es el ganador
                    if eleccion_jurado_uno == eleccion_jurado_dos or eleccion_jurado_uno == eleccion_jurado_tres:
                        ganador = eleccion_jurado_uno
                    else:
                        ganador = eleccion_jurado_dos
                else:
                    # Si todos votan diferente, se elige un ganador aleatoriamente
                    ganador = random.choice(list(elecciones))
                
                print(f"El ganador es el participante: {ganador}")















                """
                (mostrar_votos(mayor_promedios))
                eleccion_jurado_uno = int(input("Ingrese el participante que desea que gane el jurado 1: "))
                eleccion_jurado_dos = int(input("Ingrese el participante que desea que gane el jurado 2: "))
                eleccion_jurado_tres = int(input("Ingrese el participante que desea que gane el jurado 3: "))      
                ganador = None
                if eleccion_jurado_uno == eleccion_jurado_dos and eleccion_jurado_dos == eleccion_jurado_tres:
                    ganador = eleccion_jurado_uno
                elif eleccion_jurado_uno == eleccion_jurado_dos:
                    ganador = eleccion_jurado_uno
                elif eleccion_jurado_uno == eleccion_jurado_tres:
                        ganador = eleccion_jurado_uno
                elif eleccion_jurado_dos == eleccion_jurado_tres:
                    ganador = eleccion_jurado_tres
                else: 
                    ganador = random.randint(0,len(mayor_promedios))
                print(f"El ganador es el participante: {ganador}")
                """
                
        case 9:
            #Salir del programa
            print("Saliendo...")
            break
        case _:
            #Si eligen una opcion fuera del rango
            print("Opcion fuera de rango")
