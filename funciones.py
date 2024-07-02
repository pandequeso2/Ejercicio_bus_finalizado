#Funciones Principal: 
import os, time,msvcrt
import csv

bus=[['O'for x in range(4)]for y in range(7)]  #Esto nos sirve para poder crear la imagen de el bus
pasaje=5000
ventas=[]

def menu():
    while True:
        os.system('cls')
        print('\tMenu')
        print('1. Mostrar asientos.')
        print('2. Comprar asientos.')
        print('3. Mostrar ventas.')
        print('4. Exportar a csv.')
        print('5. Salir.')
        opc=validar_opc()
        os.system('cls')
        if opc==1:
            mostrar_asientos()
        elif opc==2:
            comprar_asientos()
        elif opc==3:
            mostrar_ventas()
        elif opc==4:
            exportar_csv()
        else:
            salir()
def mostrar_asientos():
    cont = 1
    print(' ASIENTOS DE BUS.')
    print('    1 2 3 4')
    print('   __________')
    for fila in bus:
        print(cont,'|',end=' ')
        for asiento in fila:
            print(asiento,end=' ')
        print('|')
        cont+=1
    print('   _________')
    msvcrt.getch()            

def comprar_asientos():
    hay_asiento=False
    for fila in bus:
        for asiento in fila:
            if asiento=='O':
                hay_asiento=True
                break
    if not hay_asiento:
        print('NO HAY ASIENTOS DISPONIBLES..')
    print('Comprar asientos.')
    nombre=validar_nombre()
    edad=validar_edad()
    telefono=validar_telefono() 
    print('... ahora selecione su asiento.')
    time.sleep(1)  
    while True:     #este ciclo while esta para ver si el asiento esta disponible, si no lo esta se busca otro
        os.system('cls')
        mostrar_asientos()
        fila = validar_numero("fila", [1,2,3,4,5,6,7])  # Esto nos permite usar una funcion para ambos valores, fila = 1,2,3,4,5,6,7
        columna = validar_numero("columna", [1,2,3,4])  # Esto nos permite usar una funcion para ambos valores, columna= 1,2,3,4
        if bus [fila-1][columna-1]=='O':        #esto nos permite ver si el estudiante es o no estudiante.
            es_estudiante=validar_estudiante()
            if es_estudiante=='s' and edad <18:
                pagar=pasaje*0.18
            elif edad>=65:
                pagar=pasaje*0.85
            else:
                pagar=pasaje
            bus[fila-1][columna-1]='X'    #esto cambia de un O a un X
            venta=[nombre,edad,telefono,fila,columna,pagar]
            ventas.append(venta)
            break
        else:
            print('Lo siento, el asiento no esta disponible...')
            time.sleep(3)         
def mostrar_ventas():
    if not ventas:
        print('ventas vacia, ve la opción 2 primero...')
        time.sleep(2)
    else:
        acum=0    #este acumulador nos permite ver el valor total de las ventas
        print('Mostrar ventas.')
        for v in ventas:
            print(v)
            acum+=v[5]
        print('el total de las ventas es: $',acum)  
        msvcrt.getch()  
def exportar_csv():
    if not ventas:
        print('ventas vacias, ve a la opcion 2 primero...')
    else:
        nombre_archivo=validar_nombre_archivo()+'.csv'
        try:
            with open(nombre_archivo,'x') as archivo:
                escritor=csv.writer(archivo)
                escritor.writerows(ventas)
            print('Archivo creado con exito...')    
        except:
            print('Nombre ya usado...')    
def salir():
    print('Adiooos...')
    exit()
#Funciones secundarias:
def validar_opc():
    while True:
        try:
            opc=int(input('Ingrese una opción: '))
            if opc in (1,2,3,4,5):
                return opc
        except:
            print('Ingrese un número. ')
def validar_nombre():
    while True:
        nom=input('Ingrese un nombre: ')
        if len(nom.strip())>=3 and nom.isalpha:
            return nom
        else:
            print('ERROR, EL NOMBRE DEBE TENRO AL MENOS 3 CARACTERES...')
def validar_edad():
    while True:
        try:
            edad=int(input('Ingrese su edad: '))
            if edad >=10 and edad <=100:
                return edad
            else:
                print('ERROR, la edad debe ser mayor a 10 y menor a 100')
        except:
            print('ERROR, debe ser un numero entero...')                            
def validar_telefono():
    while True:
        try:
            tel=int(input('Ingrese el numero de telefono...'))
            if len(str(tel))==9 and str(tel)[0]=='9':
                return tel
            else:
                print('ERROR, el numero debe comenzar con 9, y debe tener 9 caracteres')
        except:
            print('ERROR, ingrese un numero entero...')            
def validar_numero(p_palabra,p_numero):
    while True:
        try:
            num=int(input(f'Ingrese {p_palabra}: '))
            if num in p_numero:
                return num
            else:
                print(f'ERROR,{p_palabra.upper()} DEBE ESTAR ENTRE 1 Y {p_numero[-1]}...')
        except:
            print('ERROR, DEBE SER UN NÚMERO ENTERO')    
def validar_estudiante():
    while True:
        es_estudiante=input('Indique si es estudiante(s: si, n: no): ')
        if es_estudiante.lower() in('s','n'):
            return es_estudiante.lower()
        else:
            print('ERROR, INDIQUE UNA s o n') 
def validar_nombre_archivo():
    while True:
        nom=input('Ingrese el nombre de su archivo: ')
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print('ERROR, el nombre debe tener al menos 3 caracteres')                            