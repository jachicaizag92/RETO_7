# # import pandas as pd
# import utilidades as utl

# # meses = ["Enero","Febrero","Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# # sede_uno_ventas = []
# # sede_dos_ventas = []
# # sede_tres_ventas = []
# # sede_uno_gastos = []
# # sede_dos_gastos = []
# # sede_tres_gastos = []

# # ventas_sede_uno = { "Mes": meses,
# #                     "Ventas-Sede1":sede_uno_ventas,
# #                     # "Sede2":sede_dos_ventas,
# #                     # "Sede3":sede_tres_ventas,
# #                     # "Sede1":sede_uno_gastos
# #                     }

# # for mes in meses:
# #     valor = int(input(f"ingrese el valor del mes {mes}: "))
# #     sede_uno_ventas.append(valor)
    
# # print(pd.DataFrame(ventas_sede_uno))
# def validar_numero(valor):
#     validar_numero = False
#     while validar_numero == False:

#         if not valor.isnumeric():
#             return False
#         else:
#             validar_numero = True


# num = input("ingrese el numero: ")

# if validar_numero(num):
#     print("okey es numero")
# else:
#     print("NO ES NUMERICO")


import matplotlib.pyplot as plt
import pandas as pd

meses = ["Enero","Febrero"]
sede_uno_ventas= [1,2]
sede_dos_ventas = [1,2]
sede_tres_ventas = [1,2]
sede_uno_gastos = [1,2]
sede_dos_gastos = [1,2]
sede_tres_gastos = [1,2]

ventas_gastos_sedes = { "Mes": meses,
                    "Ventas-Sede1":sede_uno_ventas,
                    # "Ventas-Sede2":sede_dos_ventas,
                    # "Ventas-Sede3":sede_tres_ventas,
                    # "Gastos-Sede1":sede_uno_gastos,
                    # "Gastos-Sede2":sede_dos_gastos,
                    # "Gastos-Sede3":sede_tres_gastos,
                }
ejem =pd.DataFrame(ventas_gastos_sedes)

plt.plot(ejem['meses'],ejem['Ventas-Sede1'])
plt.show()