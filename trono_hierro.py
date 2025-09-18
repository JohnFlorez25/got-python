# Funcion para definir quien se puede sentr en el trono de hierro
def puede_sentarse_en_el_trono(nombre, casa):
    mensaje = f"cualquier cosa {nombre} {casa}"
    if (casa == "Targaryen"):
        if(nombre != "Daenerys"):
            mensaje = f"La persona {nombre} de la {casa} se puede sentar en el trono de hierro"
    return mensaje

# Datos de Entrada
nombre_personaje = input("Ingrese el nombre del personaje: ")
casa_eot = input("Ingrese el nombre de la casa a la que pertenece: ")

#Proceso
mensaje = puede_sentarse_en_el_trono(nombre_personaje, casa_eot)

#salida
print(mensaje)