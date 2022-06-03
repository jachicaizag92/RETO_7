import pandas as pd
import matplotlib.pyplot as plt

import utilidades as utl

meses = ["Enero","Febrero","Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


sede_uno_ventas= [1,250,60,70,80,100,50,60,70,80,100,200]
sede_dos_ventas = [1,250,60,70,80,10,20,90,120,180,10,230]
sede_tres_ventas = [1,250,60,70,800,100,50,60,70,80,100,200]
sede_uno_gastos = [1,250,60,70,80,100,50,60,70,80,100,200]
sede_dos_gastos = [1,250,60,70,80,100,50,60,70,80,100,200]
sede_tres_gastos = [1,250,60,70,800,120,150,110,70,80,100,200]

ventas_gastos_sedes = { "Mes": meses,
                    "Ventas-Sede1":sede_uno_ventas,
                    "Ventas-Sede2":sede_dos_ventas,
                    "Ventas-Sede3":sede_tres_ventas,
                    "Gastos-Sede1":sede_uno_gastos,
                    "Gastos-Sede2":sede_dos_gastos,
                    "Gastos-Sede3":sede_tres_gastos,
                }
menu = 0
while (menu != 4):


############## MENU ############## 
    print("\033[1;33m" + """
----------------------------------------------------------------------
                Bienvenido al sistema de ventas y gastos
----------------------------------------------------------------------
    1. Registrar ventas por mes
    2. Registrar gastos por mes
    3. Visualizar informacion 
    4. Visualizar Graficos
    5. Salir de la aplicación
  """
          "\033[0;m")

    menu = utl.convertir_entero(input("Ingrese una opcion: "))
    utl.clear()

    #Registrar ventas por mes
    if (menu == 1):

        #Sub menu para el ingreso de datos de ventar por sede
        submenu = 0
        while (submenu != 4):

            print("\033[1;32m" + """
    ----------------------------------------------------------------------
                    INGRESO DE DATOS DE VENTAS POR SEDE
    ----------------------------------------------------------------------
        1. Ventas Sede 1
        2. Ventas Sede 2
        3. Ventas Sede 3
        4. Regresar
            """
                    "\033[0;m")
            submenu = utl.convertir_entero(input("Ingrese una opcion: "))

            #sede_1
            if submenu == 1:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede                            
                    sede_uno_ventas.append(valor)
                print(sede_uno_ventas)
            #sede_2
            if submenu == 2:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede                            
                    sede_dos_ventas.append(valor)
            #sede_3
            if submenu == 3:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede                            
                    sede_tres_ventas.append(valor)
    #Registrar ventas por mes                
    if (menu == 2):

        #Sub menu para el ingreso de datos de ventar por sede
        submenu = 0
        while (submenu != 4):

            print("\033[1;35m" + """
    ----------------------------------------------------------------------
                    INGRESO DE DATOS DE GASTOS POR SEDE
    ----------------------------------------------------------------------
        1. Gastos Sede 1
        2. Gastos Sede 2
        3. Gastos Sede 3
        4. Regresar
            """
                    "\033[0;m")
            submenu = utl.convertir_entero(input("Ingrese una opcion: "))
            
            #sede_1 - Gastos
            if submenu == 1:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede                            
                    sede_uno_gastos.append(valor)
            #sede_2 - Gastos
            if submenu == 2:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede
                    sede_dos_gastos.append(valor)
            #sede_3 - Gastos
            if submenu == 3:
                for mes in meses:
                    #Validación numero
                    validar_numero = False
                    while validar_numero == False:
                        valor = input(f"ingrese el valor del mes {mes}: ")
                        if not valor.isnumeric():
                            print("el valor no es numerico")
                        else:
                            validar_numero = True
                        #Agregamos el valor a la lista de la respectiva sede                            
                    sede_tres_gastos.append(valor)
    if (menu == 3):
        print("\033[1;36m" + """
    ----------------------------------------------------------------------
                           VISUALIZACION DE DATOS
    ----------------------------------------------------------------------\n
            """
                    "\033[0;m")
        submenu = 0
        while (submenu != 4):

            print(pd.DataFrame(ventas_gastos_sedes))
            submenu = 4
        input("\nOprima tecla enter para continuar...")
    if (menu == 4):

        submenu = 0
        while submenu != 5:    
                    
            print("\033[1;32m" + """
    ----------------------------------------------------------------------
                        VISUALIZACION DE GRAFICAS
    ----------------------------------------------------------------------\n
        1. Visualizar grafica de Barras Ventas
        2. Visualizar grafica de Barras Gastos
        3. Visualizar grafica de Lineas Ventas
        4. Visualizar grafica de Lineas Gastos
        5. regresar
            """
                    "\033[0;m")
            opc = utl.convertir_entero(input("Ingrese una opcion: "))

            if opc == 1:
                utl.clear() 
                if len(sede_uno_ventas) == 12 and len(sede_dos_ventas) == 12 and len(sede_tres_ventas) == 12:
                    utl.grafica_barras(meses,sede_dos_ventas,sede_dos_ventas,sede_tres_ventas,"GRAFICA VENTAS", "g","b")
                    submenu = 4
                else:
                    print("\033[1;31m" +"Actualmente no hay datos para graficar...\033[0;m ")
            if opc == 2:
                utl.clear() 
                if len(sede_uno_gastos) == 12 and len(sede_dos_gastos) == 12 and len(sede_tres_gastos) == 12:
                    utl.grafica_barras(meses,sede_dos_gastos,sede_dos_gastos,sede_tres_gastos,"GRAFICA GASTOS", "r", "b")
                    submenu = 4
                else:
                    print("\033[1;31m" +"Actualmente no hay datos para graficar...\033[0;m ")
            if opc == 3:
                utl.clear() 
                if len(sede_uno_ventas) == 12 and len(sede_dos_ventas) == 12 and len(sede_tres_ventas) == 12:
                    utl.grafica_barras(meses,sede_dos_ventas,sede_dos_ventas,sede_tres_ventas,"GRAFICA VENTAS", "g","l")
                    submenu = 4
                else:
                    print("\033[1;31m" +"Actualmente no hay datos para graficar...\033[0;m ")
            if opc == 4:
                utl.clear() 
                if len(sede_uno_gastos) == 12 and len(sede_dos_gastos) == 12 and len(sede_tres_gastos) == 12:
                    utl.grafica_barras(meses,sede_dos_gastos,sede_dos_gastos,sede_tres_gastos,"GRAFICA GASTOS", "r", "l")
                    submenu = 4
                else:
                    print("\033[1;31m" +"Actualmente no hay datos para graficar...\033[0;m ")
            if opc == 5:
                submenu = 5
input("\nOprima tecla enter para continuar...")
