producto = input("Introduzca el nombre del producto: ")
precio = input("Introduzca el precio del producto: ")
unidades = input("Cuántas unidades desea?: ")

entero , decimal = precio.split(",")
entero.zfill(6)
decimal.zfill(2)

preciofinal = float(precio*unidades)
preciofinal = str(preciofinal)
enteropf , decimalpf = preciofinal.split(",")
enteropf.zfill(8)
decimalpf.zfill(2)


unidades.zfill(3)

print ("El producto",producto,
       "Tiene un precio unitario de", entero + "," + decimal,
       " Y", unidades, "Tendrían un coste total de", enteropf + "," + decimalpf)
