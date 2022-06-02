from os import system, name



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