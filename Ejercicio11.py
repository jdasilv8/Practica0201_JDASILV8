producto = input("Introduzca el nombre del producto: ")
precio = float(input("Introduzca el precio del producto (separar € y céntimos con .: "))
unidades = int(input("Cuántas unidades desea?: "))

preciofinal = float(precio * unidades)

precio = str(precio)
unidades = str(unidades)
preciofinal = str(preciofinal)

entero , decimal = precio.split(".")
entero.zfill(6)
decimal.zfill(2)

enteropf , decimalpf = preciofinal.split(".")
enteropf.zfill(8)
decimalpf.zfill(2)


unidades.zfill(3)
print (entero)
print ("El producto",producto,
       "Tiene un precio unitario de", entero + "," + decimal,
       " Y", unidades, "Tendrían un coste total de", enteropf + "," + decimalpf)
