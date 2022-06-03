from os import system, name
import matplotlib.pyplot as plt


def convertir_entero (valor):
    """Funcion encargada de convertir cadena de texto a numeros enteros

    Args:
        valor (_type_): string

    Returns:
        int: retorna el entero, en caso contrario retorna el 0
    """

    try:
        entero = int(valor)
        return entero
    except ValueError:
        return 0

def clear():
    """Funcion encargada de limpiar pantalla para terminal windows, linux o mac
    """

    if name == 'nt':
        _= system('cls')
    else:
	    _= system('clear')

def grafica_barras(meses:list,sede_1:list,sede_2:list,sede_3:list,titulo:str,color:str,tipo:str):
    """funcion encargada de graficar las dos graficas de barras y de lineas de acuerdo al parametro establecido

    Args:
        meses (list): lista con los meses (eje x)
        sede_1 (list): lista con los valores de las sede_1 (eje y)
        sede_2 (list): lista con los valores de las sede_2 (eje y)
        sede_3 (list): lista con los valores de las sede_3 (eje y)
        titulo (str): titulo para la agrupacion de la grafica y titulo de descarga
        color (str): color de las graficas
        tipo (str): tipo de grafica puede ser => "l" = lineal, "b" = barras
    """

    if tipo == 'b':
        fig,ventas_sedes=plt.subplots(3,1,figsize=(12,7.5),label=f"{titulo}")
        plt.suptitle(f'{titulo}',fontsize=20, color=f"{color}")
        ventas_sedes[0].bar(meses,sede_1, color=f"{color}", width=0.7)
        ventas_sedes[0].legend(["SEDE 1"])
        ventas_sedes[1].bar(meses,sede_2, color=f"{color}", width=0.7)
        ventas_sedes[1].legend(["SEDE 2"])
        ventas_sedes[2].bar(meses,sede_3, color=f"{color}", width=0.7)
        ventas_sedes[2].legend(["SEDE 3"])
        plt.show()
    elif tipo == 'l':
        fig,ventas_sedes=plt.subplots(3,1,figsize=(12,7.5),label=f"{titulo}")
        plt.suptitle(f'{titulo}',fontsize=20, color=f"{color}")
        ventas_sedes[0].plot(meses,sede_1, color=f"{color}")
        ventas_sedes[0].legend(["SEDE 1"])
        ventas_sedes[1].plot(meses,sede_2, color=f"{color}")
        ventas_sedes[1].legend(["SEDE 2"])
        ventas_sedes[2].plot(meses,sede_3, color=f"{color}")
        ventas_sedes[2].legend(["SEDE 3"])
        plt.show()       