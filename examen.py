import os
import Hola as h
os.system('cls')

while True:
    opc=h.menu_1('menu principal',['selecciona empleado','ingresa sueldo','clasificacion de sueldo','reporte de sueldos'])
    if opc==1:
        emp=h.empleado_1()
    elif opc==2:
        sueldo=h.money()
    elif opc==3:
        emp=h.cla_sueldo()
    elif opc==4:
        emp=h.rep_sueldo()
    elif opc==5:
        print('termiando programa...\nDesarrollado por Ignacio Sepulveda\nRut 21.453.402-9')
        break