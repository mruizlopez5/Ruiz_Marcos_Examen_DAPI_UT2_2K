clientes={}
aprobados={}
z = True

def añadir_cliente():
    nombre = input("introduce nombre y apellidos del cliente: ")
    aprobado= input("introduce si es abonado: 'si' o 'no': ").lower()
    
    if aprobado == "si":
        clientes[nombre]=True
    else:
        clientes[nombre]=False  
    print("cliente Añadido a la base\n")
    return
        


def mostrar_clientes():
    print(clientes,"\n")
    return


def numero_suscritos():
    for nombre in clientes:
        if clientes[nombre] == True:
            aprobados[nombre]=clientes[nombre]
    print(aprobados,"\n")
        

while z == True:

    seleccion = input("""introduzca una opcion:
        1 Añadir cliente. 
        2 Numero de suscritos. 
        3 Mostrar todos los clientes.  
        4 Terminar. (reiniciar)\n""")

    if seleccion == "":
            ""
    elif int(seleccion) == 1:
        añadir_cliente()
    elif int(seleccion) == 2:
        numero_suscritos()
    elif int(seleccion) == 3:
        mostrar_clientes()
    elif int(seleccion) == 4:
        z=False
    else:
           ""