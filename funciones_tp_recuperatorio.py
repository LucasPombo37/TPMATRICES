from constantes import *

#MENU
#------

def menuu()->int:
    """
    Muestra el menú principal del programa con las distintas opciones disponibles.

    Retorna:
        int: Opción seleccionada por el usuario.
    """
    print(f"----MENU DEL PROGRAMA----\n1.Cargar notas\n2.Mostrar votos\n3.Ordenar votos\n4.Peores 3\n5.Mayores promedios\n6.Jurado malo\n7.Sumatoria\n8.Definir ganador\n9.Salir del programa")
    return int(input("Ingrese una opción: "))

#Inicializar matriz
#------------------

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any)->list:
    """
    Crea e inicializa una matriz con un valor inicial.

    Parámetros:
    cantidad_filas (int): Número de filas de la matriz.
    cantidad_columnas (int): Número de columnas de la matriz.
    valor_inicial (any): Valor inicial con el cual se llenarán todas las posiciones de la matriz.

    Retorna:
    list: Una matriz (lista de listas) de dimensiones `cantidad_filas` x `cantidad_columnas`, 
          en la cual cada elemento está inicializado con `valor_inicial`.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#Validar datos
#-----------------
def validar_votos(mensaje:str,mensaje_error:str,minimo:int,maximo:int)->float:
    """
    Solicita al usuario un número dentro de un rango válido.

    Parámetros:
        mensaje (str): Mensaje mostrado al solicitar el dato.
        mensaje_error (str): Mensaje mostrado en caso de error.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Retorna:
        float: Número válido ingresado por el usuario.
    """
    dato = float(input(mensaje))
    while dato < minimo or dato > maximo:
        #Volver a pedir el dato si esta fuera de rango
        dato = float(input(mensaje_error))
    return dato


#Mostrar lista
def mostrar_lista(participantes:list):
    """
    Muestra los datos de los participantes

    Parametros:
        participantes(list) : Lista de participantes
    No retorna ninguna valor. La funcion imprime la lista formateada
    """
    # Mostrar el encabezado
    print("Participante   |   Nota jurado 1   |   Nota jurado 2   |   Nota jurado 3   |   Nota Promedio")
    # Iterar sobre los participantes y mostrar los datos
    for i in range(len(participantes)):
        # Imprimir cada fila de la matriz de forma legible
        print("     " + str(participantes[i][0]) + "      |     " + str(participantes[i][1]) + 
              "        |     " + str(participantes[i][2]) + "        |     " + str(participantes[i][3]) + 
              "        |     " + str(participantes[i][4]))

#Mostrar matriz
#----------------
def mostrar_votos(participantes:list):
    """
    Muestra los datos de los participantes, incluyendo las notas y el promedio.

    Parámetros:
        participantes (list): Matriz de participantes con notas y promedios.

    No retorna ningún valor. La función imprime la matriz formateada.
    """
    # Mostrar el encabezado
    print("Participante   |   Nota jurado 1   |   Nota jurado 2   |   Nota jurado 3   |   Nota Promedio")
    print("-" * 74)  # Línea separadora para mayor claridad

    # Iterar sobre los participantes y mostrar los datos
    for i in range(len(participantes)):
        # Imprimir cada fila de la matriz de forma legible y alineada
        print(f"{str(participantes[i][0]):<15} | {str(participantes[i][1]):<17} | {str(participantes[i][2]):<17} | {str(participantes[i][3]):<17} | {str(participantes[i][4]):<15}")



#Cargar datos
#--------------
def cargar_votos(participantes:list)->list:
    """   
    Permite ingresar las notas de los jurados para cada participante.

    Parámetros:
        participantes (list): Matriz donde se cargarán las notas.

    Retorna:
        list: Matriz de participantes actualizada con notas y promedios.
    
    """
    for i in range(len(participantes)):
        for j in range(len(participantes[i])):
            if j == ID:
                #Asignar ID de participante
                participantes[i][ID] = i+1
            elif j == I_PROMEDIO:
                #Calcular el promedio de los votos
                participantes[i][I_PROMEDIO] = calcular_promedio(participantes[i])
            else:
                #Validar y cargar los votos de los jurados
                participantes[i][j] = validar_votos(f"Ingrese voto del jurado {j} (Debe ser entre 1 y 100) ","Error/ debe estar en el rango de 1 y 100 ",1,100)      
    return participantes


#Ordenar notas
#--------------
#asc o desc

def ordenar_votos(participantes:list,opcion:str)->list:
    """
    Ordena la matriz de participantes según sus promedios.

    Parámetros:
        participantes (list): Matriz de participantes a ordenar.
        opcion (str): Dirección de ordenamiento: "asc" (ascendente) o "desc" (descendente).

    Retorna:
        list: Matriz de participantes ordenada.
    """
   
    if opcion == "asc":
        ordenar_participantes_asc(participantes)   
    elif opcion == "desc":
        ordenar_participantes_desc(participantes)
    else:
        #Mensaje de error para opcion invalida
        return ("Opcion Invalida")
    return participantes

def ordenar_participantes_asc(participantes:list)->list:
    """
    Esta funcion recibe como parametro una lista
    Devuelve una lista ordenada de forma ascendente
    """
    for i in range(len(participantes)-1):
        for j in range(i+1,len(participantes)):
            if participantes[i][I_PROMEDIO] > participantes[j][I_PROMEDIO]:
                intercambiar_matriz(participantes,i,j)
    return participantes

def ordenar_participantes_desc(participantes:list)->list:
    """
    Esta funcion recibe como parametro una lista
    Devuelve una lista ordenada de forma descendente
    """
  
    for i in range(len(participantes)-1):
        for j in range(i+1,len(participantes)):
            if participantes[i][I_PROMEDIO] < participantes[j][I_PROMEDIO]:
                intercambiar_matriz(participantes,i,j)
    return participantes

def intercambiar_matriz(matriz, i, j):
    """
    Intercambia dos filas en la matriz.

    Parámetros:
    matriz (list): La matriz de listas a modificar.
    i (int): Índice de la primera fila a intercambiar.
    j (int): Índice de la segunda fila a intercambiar.

    Esta función intercambia los elementos en las posiciones `i` y `j` 
    dentro de la matriz proporcionada, utilizando una variable auxiliar.
    """
    auxiliar = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = auxiliar


#Calcular promedio
#------------------
def calcular_promedio(vector: list)->float:
    """
    Calcula el promedio de las notas en un vector.

    Parámetros:
        vector (list): Vector con las notas de un participante.

    Retorna:
        float: Promedio de las notas (excluyendo el ID y el promedio).
    """
    acumulador = 0

    for i in range(len(vector)):
        #Que no pertenezcan a ninguno de los dos indices      
        if i != ID and i != I_PROMEDIO:
            acumulador += vector[i]

    #Divido por la cantidad de notas
    return acumulador / 3

#Peores 3
#---------

def peores_tres(participantes:list):
    """
    Encuentra los tres participantes con los promedios más bajos.

    Parámetros:
        participantes (list): Matriz de participantes.

    Retorna:
        list: Matriz con los datos de los tres participantes con los peores promedios.
    """

    #Creo una lista con 3 lugares
    tres_peores = [0,0,0]

    #Ordeno la lista de participantes de forma ascendente
    ordenar_participantes_asc(participantes)

    for i in range(3):
        # Almacenar los tres primeros después de ordenar
        tres_peores = participantes[i]
    
    #Retorno los peores 3
    return tres_peores
        
def promedio_general(participantes:list)->float:
    """
    Calcula el promedio general de todos los promedios de los participantes.

    Parámetros:
        participantes (list): Matriz de participantes.

    Retorna:
        float: Promedio general de los promedios.
    """
    acumulador = 0
    contador = 0
    for i in range(len(participantes)):
        acumulador += participantes[i][I_PROMEDIO]
        contador += 1
    promedio_genral = acumulador / contador
    return promedio_genral


def mayores_promedios(participantes:list)->list:
    """
    Encuentra a los participantes cuyos promedios superan el promedio general.

    Parámetros:
        participantes (list): Matriz de participantes.

    Retorna:
        list: Matriz con los datos de los participantes que superan el promedio general.
    """
    acumulador = 0
    promedio_genral = promedio_general(participantes)

    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] > promedio_genral:
            # Cuento cuántos participantes superan el promedio general
            acumulador += 1

    #Inicializo una matriz 
    mayores_promedios = inicializar_matriz(acumulador, 5, 0)
    fila_actual = 0  # Índice para las filas de mayores_promedios

    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] > promedio_genral:
            mayores_promedios[fila_actual] = participantes[i]
            fila_actual += 1  # Avanzar al siguiente índice

    return mayores_promedios


def jurado_malo(participante:list)->list:
    """
    Encuentra cuál jurado puso las notas más bajas en promedio.

    Parámetros:
        participante (list): Lista con los datos de los participantes, 
                             incluyendo las notas de tres jurados.

    Retorna:
        list: Contiene dos valores:
            - El número del jurado (1, 2 o 3) que tiene el promedio más bajo.
            - El promedio más bajo de ese jurado.

    """
    
    suma_jurados = [0,0,0]
    cantidad_participantes = len(participante)

    #Cargo la lista con las notas de los 3 jurados
    for i in range(len(participante)):
        suma_jurados[0] += participante[i][NOTA_UNO]         
        suma_jurados[1] += participante[i][NOTA_DOS]           
        suma_jurados[2] += participante[i][NOTA_TRES]
            
    #Calcular ahora el promedio de los jurados
    promedio_jurados = [
        suma_jurados[0] / cantidad_participantes,
        suma_jurados[1] / cantidad_participantes,
        suma_jurados[2] / cantidad_participantes,
    ]

    # Encontrar el menor promedio entre los jurados
    peor_jurado = [0,0]
    jurado_peor_promedio = 0
    peor_promedio = promedio_jurados[0]
    
    for i in range(len(promedio_jurados)):
        if promedio_jurados[i] <= peor_promedio:
            peor_promedio = promedio_jurados[i]
            jurado_peor_promedio = i+1
       
    peor_jurado[0] = jurado_peor_promedio
    peor_jurado[1] = peor_promedio
    return peor_jurado


   
def sumar_notas(participantes:list,numero_objetivo:int):
    """
    Encuentra los participantes cuya suma de notas coincide con un número objetivo.

    Parámetros:
        participantes (list): Matriz que contiene los datos de los participantes, 
                              incluyendo sus notas.
        numero_objetivo (int): Número al que debe coincidir la suma de las notas.

    Retorna:
        list: Matriz de participantes cuyas notas suman el número objetivo.
        str: Mensaje de error si no hay coincidencias.
    """
    acumulador = 0
    contador = 0

    # Primera pasada: contar cuántos participantes tienen suma de notas igual al objetivo
    for i in range(len(participantes)):    
            suma_notas = 0
            for j in range(len(participantes[i])):
                if j != ID and j != I_PROMEDIO:
                    suma_notas += participantes[i][j]  # Sumar las notas usando índices

                    if suma_notas == numero_objetivo:
                        acumulador += 1

    # Inicializamos la matriz para almacenar los participantes coincidentes
    participantes_coincidencia = inicializar_matriz(acumulador,5,0)

    # Segunda pasada: guardar los participantes que cumplen con la condición
    for i in range(len(participantes)):
            suma_notas = 0
            for j in range(len(participantes[i])):
                if j != ID and j != I_PROMEDIO:
                    suma_notas += participantes[i][j]  # Sumar los votos de los jurados          
                    if suma_notas == numero_objetivo:               
                        participantes_coincidencia[contador] = participantes[i]
                        contador += 1 # Incrementar contador si la suma coincide

    #Mensaje en caso de no encontrar coincidencias
    mensaje_error = "No hay coincidencias"

    # Verificar si hubo coincidencias en las sumas de notas
    if acumulador == 0:
        # Si no se encontraron coincidencias, devolver un mensaje de error
        return mensaje_error 
    else:   
        # Si hay coincidencias, devolver la matriz con los participantes correspondientes
        return participantes_coincidencia




def calcular_promedio_maximo(participantes: list)->float:
    """
    Encuentra el promedio máximo de los participantes.

    Parámetros:
        participantes (list): Matriz que contiene los datos de los participantes,
                              incluyendo sus promedios.

    Retorna:
        float: El promedio máximo encontrado en los participantes.
    """
    maximo = participantes[0][I_PROMEDIO]  # Suponemos que el primero tiene el mayor promedio
    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] > maximo:
            maximo = participantes[i][I_PROMEDIO]
    return maximo

def obtener_participantes_con_promedio_maximo(participantes: list, maximo: float)->list:
    """
    Obtiene a los participantes cuyo promedio es el máximo.

    Parámetros:
        participantes (list): Matriz que contiene los datos de los participantes, 
                               incluyendo sus promedios.
        maximo (float): El promedio máximo a comparar.

    Retorna:
        list: Matriz con los participantes que tienen el promedio máximo.
    """

    """
    # Inicializar una lista para almacenar a los participantes con el promedio máximo
    mayores_prom = inicializar_matriz(contador, 5, 0)  # Inicializar matriz vacía con 0 filas por ahora
    contador = 0  # Contador para el índice de la nueva matriz
    
    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] == maximo:
            mayores_prom[contador] = participantes[i] # Asignar el participante a la fila correspondiente
            contador += 1 # Incrementar el contador para la siguiente fila

    return mayores_prom
    """
    # Contar cuántos participantes tienen el promedio máximo
    contador = 0
    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] == maximo:
            contador += 1

    # Crear la matriz con el tamaño adecuado
    mayores_prom = inicializar_matriz(contador, 5, 0)  # Inicializar matriz con el número correcto de filas
    contador = 0  # Reiniciar el contador para agregar los participantes

    # Agregar los participantes con el promedio máximo
    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] == maximo:
            mayores_prom[contador] = participantes[i]
            contador += 1

    return mayores_prom

def mayor_promedio(participantes:list):
    """
    Encuentra a los participantes con el mayor promedio de notas.

    Parámetros:
        participantes (list): Matriz que contiene los datos de los participantes,
                              incluyendo sus promedios.

    Retorna:
        list: Matriz de participantes que tienen el promedio más alto.
    """
    # Usar la función para obtener el promedio maximo
    maximo = calcular_promedio_maximo(participantes)
   
    # Contar y almacenar a los participantes con el promedio máximo
    mayores_prom = obtener_participantes_con_promedio_maximo(participantes, maximo)

    return mayores_prom # Retornar la matriz con los participantes que tienen el promedio más alto


               
def mayor_promediosss(participantes:list):
    """
    Encuentra a los participantes con el mayor promedio de notas.

    Parámetros:
        participantes (list): Matriz que contiene los datos de los participantes,
                              incluyendo sus promedios.

    Retorna:
        list: Matriz de participantes que tienen el promedio más alto.
    """
    # Encontrar el promedio máximo en la matriz
    maximo = participantes[0][I_PROMEDIO] # Suponemos que el primero tiene el mayor promedio
    contador = 0
    
    # Primera pasada: determinar el promedio máximo
    for i in range(len(participantes)):
        for j in range(len(participantes[i])):
            if j == I_PROMEDIO:
                if participantes[i][I_PROMEDIO] > maximo:
                    maximo = participantes[i][I_PROMEDIO]

    # Segunda pasada: contar cuántos participantes tienen el promedio máximo
    for i in range(len(participantes)):
        for j in range(len(participantes[i])):
            if j == I_PROMEDIO and participantes[i][j] == maximo:
                contador += 1

    # Crear una matriz para almacenar a los participantes con el mayor promedio
    mayores_prom = inicializar_matriz(contador,5,0)
    contador = 0 # Reiniciar contador para usarlo como índice

    # Tercera pasada: guardar a los participantes con el promedio máximo
    for i in range(len(participantes)):
        for j in range(len(participantes[i])):
            if j == I_PROMEDIO and participantes[i][j] == maximo:
                mayores_prom[contador] = participantes[i]
                contador += 1

    return mayores_prom # Retornar la matriz con los participantes que             









        
        

                




""""
def peores_jurados(participantes:list):
    
    acumulador = 0
    promedio_genral = promedio_general(participantes)

    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] < promedio_genral:
            # Cuento cuántos participantes superan el promedio general
            acumulador += 1

    mayores_promedios = inicializar_matriz(acumulador, 5, 0)

    fila_actual = 0  # Índice para las filas de mayores_promedios
    for i in range(len(participantes)):
        if participantes[i][I_PROMEDIO] > promedio_genral:
            mayores_promedios[fila_actual] = participantes[i]
            fila_actual += 1  # Avanzar al siguiente índice

    return mayores_promedios
"""



