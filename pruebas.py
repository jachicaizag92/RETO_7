
from turtle import color
# import matplotlib.pyplot as plt 
import utilidades as utl
import matplotlib.pyplot as plt


meses = ["Enero","Febrero","Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
sede_uno_ventas= [1,250,60,70,80,100,50,60,70,80,100,200]
sede_dos_ventas = [1,250,60,70,80,10,20,90,120,180,10,230]
sede_tres_ventas = [1,250,60,70,800,100,50,60,70,80,100,200]
sede_uno_gastos = [1,250,60,70,80,100,50,60,70,80,100,200]
sede_dos_gastos = [1,250,60,70,80,100,50,60,70,80,100,200]
sede_tres_gastos = [1,250,60,70,800,120,150,110,70,80,100,200]

# print(len(meses, sede_dos_gastos))


# fig,ventas_sedes=plt.subplots(3,1,figsize=(12,7.5),label="Grafico de ventas por sedes")
# plt.suptitle('GRAFICO DE VENTAS POR SEDES',fontsize=20, color="g")
# ventas_sedes[0].bar(meses,sede_uno_ventas, color="g", width=0.7)
# ventas_sedes[0].legend(["SEDE 1"])
# ventas_sedes[1].bar(meses,sede_dos_ventas, color="g", width=0.7)
# ventas_sedes[1].legend(["SEDE 2"])
# ventas_sedes[2].bar(meses,sede_tres_ventas, color="g", width=0.7)
# ventas_sedes[2].legend(["SEDE 3"])
# plt.show()

# fig,ventas_sedes=plt.subplots(3,1,figsize=(12,7.5),label="Grafico de ventas por sedes")
# plt.suptitle('GRAFICO DE VENTAS POR SEDES',fontsize=20, color="r")
# ventas_sedes[0].plot(meses,sede_uno_gastos, color="r")
# ventas_sedes[0].legend(["SEDE 1"])
# ventas_sedes[1].plot(meses,sede_dos_gastos, color="r")
# ventas_sedes[1].legend(["SEDE 2"])
# ventas_sedes[2].plot(meses,sede_tres_gastos, color="r")
# ventas_sedes[2].legend(["SEDE 3"])
# plt.show()

utl.grafica_barras(meses,sede_dos_ventas,sede_dos_ventas,sede_tres_ventas,"GRAFICA VENTAS", "y","b")