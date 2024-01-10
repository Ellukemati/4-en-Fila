import cuatro_en_linea

def main():
    cuatro_en_linea.presentar_programa()

    while True:
        tablero = cuatro_en_linea.pedir_tablero()

        while True:
            cuatro_en_linea.imprimir_tablero(tablero)
            cuatro_en_linea.realizar_turno(tablero)
            if cuatro_en_linea.anunciar_ganador(tablero):
                if cuatro_en_linea.fin_del_juego():
                    break

main()
