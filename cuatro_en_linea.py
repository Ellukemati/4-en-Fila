from typing import List

# LÓGICA DEL JUEGO
def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """
    tablero = []

    for i in range(n_filas):
        fila_nueva = []
        for j in range(n_columnas):
            fila_nueva.append(" ")
        tablero.append(fila_nueva)

    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    contador_x = 0
    contador_o = 0

    for fila in tablero:
        for columna in fila:
            if columna == "X":
                contador_x += 1
            if columna == "O":
                contador_o += 1

    if contador_x <= contador_o:
        return True
    return False

def encontrar_fila_libre(tablero: list[list[str]], columna: int) -> int:
    """
    FUNCIÓN AUXILIAR PROPIA

    Dado un tablero y un número de columna, busca la fila más baja del tablero que esté libre para insertarle un símbolo.

    PRECONDICIONES:
        - el número de columna debe estar dentro del rango de columnas del tablero. Caso contrario devuelve -1.
    POSTCONDICIONES:
        - si la función devuelve un número positivo, éste es el número de fila libre más bajo en el tablero para
        insertar un símbolo dentro de la columna dada. Si devuelve -1, la columna está llena y no puede insertarse
        ningún símbolo o la columna dada no está en el rango.
    """
    fila_libre = -1

    if columna >= len(tablero[0]) or columna < 0:
        return fila_libre

    for fila in range(len(tablero)):
        if tablero[fila][columna] == " ":
            fila_libre = fila
        else:
            break

    return fila_libre

def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """
    fila_libre = encontrar_fila_libre(tablero, columna)
    if fila_libre == -1:
        return False

    if es_turno_de_x(tablero) == True:
        tablero[fila_libre][columna] = "X"
        return True
    else:
        tablero[fila_libre][columna] = "O"
        return True

def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    contador_de_columnas_llenas = 0

    for columna in tablero[0]:
        if columna == " ":
            return False
        else:
            contador_de_columnas_llenas += 1
            if contador_de_columnas_llenas == len(tablero[0]):
                return True

def está_en_tablero(tablero: list[list[str]], fila: int, columna: int) -> bool: return 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])

def cuatro_en_fila(tablero: list[list[str]], fila: int, columna: int) -> bool:
    """
    FUNCIÓN AUXILIAR PROPIA

    Revisa la posición dada está en tablero y chequea las posibles posiciones de victoria, devolviendo True en caso de que la haya.
    """
    if está_en_tablero(tablero, fila, columna + 3) and tablero[fila][columna] == tablero[fila][columna + 1] == tablero[fila][columna + 2] == tablero[fila][columna + 3]:
        return True
    elif está_en_tablero(tablero, fila + 3, columna) and tablero[fila][columna] == tablero[fila + 1][columna] == tablero[fila + 2][columna] == tablero[fila + 3][columna]:
        return True
    elif está_en_tablero(tablero, fila + 3, columna + 3) and tablero[fila][columna] == tablero[fila + 1][columna + 1] == tablero[fila + 2][columna + 2] == tablero[fila + 3][columna + 3]:
        return True
    elif está_en_tablero(tablero, fila + 3, columna - 3) and tablero[fila][columna] == tablero[fila + 1][columna - 1] == tablero[fila + 2][columna - 2] == tablero[fila + 3][columna - 3]:
        return True
    return False

def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O', 'O', 'X', 'X', 'X', 'O'],
        ]
    """
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] != " " and cuatro_en_fila(tablero, fila, columna):
                return tablero[fila][columna]
    return " "

# INTERACCIÓN CON EL USUARIO / VISUALES

def presentación_del_juego(título: str):
    print("╔" + "═" * len(título) + "╗")
    print("║" + título + "║")
    print("╚" + "═" * len(título) + "╝")

def salir_del_juego():
    print("Saliendo del juego...")
    quit()

def pedir_tablero() -> list[list[str]]:
    """
    FUNCIÓN AUXILIAR PROPIA

    Pide al usuario un alto y un ancho dentro del rango hasta que ambos son válidos.
    Cuando lo son, crea un tablero con estas dimensiones y lo devuelve.
    """
    mensaje_entrada_inválida = "Entrada fuera de rango o no es un carácter válido. Ingrese nuevamente."

    print()
    while True:
        alto = input("Ingrese el ALTO del tablero (Entre 4 y 10) o 'x' para salir: ")
        if alto.lower() == "x":
            salir_del_juego()
        if alto.isdecimal() and 4 <= int(alto) <= 10:
            break
        else:
            print(mensaje_entrada_inválida)

    while True:
        ancho = input("Ingrese el ANCHO del tablero (Entre 4 y 10) o 'x' para salir: ")
        if ancho.lower() == "x":
            salir_del_juego()
        if ancho.isdecimal() and 4 <= int(ancho) <= 10:
            return crear_tablero(int(alto), int(ancho))
        else:
            print(mensaje_entrada_inválida)

def imprimir_tablero(tablero: list[list[str]]):
    """
    FUNCIÓN AUXILIAR PROPIA

    Imprime el tablero dado en un formato agradable para el usuario.
    """
    print()
    columnas = len(tablero[0])
    for i in range(0, columnas):
        print("|" + str(i), end="")
    print("|")
    print("-" * (len(tablero[0]) * 2 + 1))
# Esto imprime el contador de columnas de la parte superior, junto a una linea horizontal que lo separa del tablero

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            print(tablero[fila][columna].rjust(2, "|"), end="")
        print("|")
    print("-" * (len(tablero[0]) * 2 + 1))
# Esto imprime el tablero y una línea horizontal en el fondo



def realizar_turno(tablero: list[list[str]]):
    """
    FUNCIÓN AUXILIAR PROPIA

    Pide al usuario un número de columna hasta que ingrese uno válido, y si lo es, inserta el símbolo
    correspondiente en la columna elegida.
    """
    if es_turno_de_x(tablero):
        jugador_actual = "X"
    else:
        jugador_actual = "O"

    while True:
        columna_elegida = input("Ingrese una columna entre 0 y " + str(len(tablero[0]) - 1) + " para insertar una ficha de " + jugador_actual + " o ingrese 'x' para salir: ")
        if columna_elegida.lower() == "x":
            salir_del_juego()
        if columna_elegida.isdecimal():
            if 0 <= int(columna_elegida) <= len(tablero[0]) - 1:
                if encontrar_fila_libre(tablero, int(columna_elegida)) == -1:
                    print("Columna llena. Ingrese nuevamente.")
                else:
                    insertar_simbolo(tablero, int(columna_elegida))
                    break
            else:
                print("La columna ingresada está fuera de rango. Ingrese nuevamente.")
        else:
            print("La entrada no es un carácter válido. Ingrese nuevamente.")


def anunciar_ganador(tablero: list[list[str]]) -> bool:
    """
    FUNCIÓN AUXILIAR PROPIA

    Chequea las condiciones de final de partida e imprime un mensaje final a la vez que
    devuelve un booleano acorde a la finalización de la misma.
    """
    ganador = obtener_ganador(tablero)

    if ganador != " ":
        imprimir_tablero(tablero)
        print(f"¡{ganador} es el GANADOR! Gracias por jugar.")
        return True
    elif tablero_completo(tablero):
        imprimir_tablero(tablero)
        print("El tablero está completo y sin ganadores, EMPATE. Gracias por jugar.")
        return True

    return False

def fin_del_juego() -> bool:
    print()
    print("1. Jugar otra partida.")
    print("2. Salir del juego.")
    while True:
        opción = input("Ingrese opción deseada: ")
        if opción == "2":
            salir_del_juego()
        if opción == "1":
            return True
        else:
            print("La entrada no es válida. Ingrese nuevamente.")
            continue
