def menu_1(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')
def negro(emple):
    return emple in ['j','ma','c','a','p','l','mi','i','f','e']

def empleado_1():
    while True:
        emplea={'j':'juan perez', 'ma':'maria garcia','c':'carlos lopez','a':'ana martinez','p':'pedro rodriguez','l':'laura hernandez','mi':'miguel sanchez','i':'isabel gomez','f':'francisco diaz','e':'elena fernandez'}
        while True:
            emple=input('\nElije un Empleado\nj = juan perez\nma = maria garcia\nc = carlos lopez\na = ana martinez\np = pedro rodriguez\nl = laura hernandez\nmi = miguel sanchez\ni = isabel gomez\nf = francisco diaz\ne = elena fernandez\nselecciona uno :')
            if negro(emple):
                return emplea.get(emple)
            else:
                print('empleado erroneo')

def money():
    while True:
        dinero=int(input('Ingresa el salario del empleado minimo $300000 maximo $2500000\n'))
        if dinero<300000 or dinero>2500000:
            print('dinero no valido, vuelva a ingresar.')
        elif dinero>299999 or dinero<2500001:
            print('dinero valido.')
            return opc_int

def cla_sueldo():
    #if:
    #print('sueldo menor a $800000 total :',len(empleado_1))
    #print()

def rep_sueldo():
        print('nombre empleado---sueldo base---desc salud---desc AFP---sueldo liquido\n')
        afp=money*0.07
        salud=money*0.12
        liquido=(money-afp-salud)
        print(empleado_1,         money,       afp,   salud,    liquido)
        print('')