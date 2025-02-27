def calculadora_iva(nombre, precio):
    

    diccionario = {}
    diccionario[nombre]=round((precio*(1.21)),3)
    
    return diccionario

def archivo_listado(dicc):
    titulo = "listado_de_precios.txt"
    txt = open(titulo, "a")
    txt.write(str(dicc) + "\n")
    txt.close()
    txt = open(titulo, "r")
    print(txt.read())
    txt.close()
    return 0

NombreProducto = input("introduce nombre del producto: ")
PrecioProducto = float(input("introduce precio de producto: ").replace(",","."))
archivo_listado(calculadora_iva(NombreProducto, PrecioProducto))
