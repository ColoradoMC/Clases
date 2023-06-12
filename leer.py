archivo=open("archivo.txt", "r")
while True:
    nombre=input("Nombre: ")
    telefono=input("Telefono")
    mail=input("Mail: ")
    archivo.write(f"Nombre: {nombre}, Teléfono: {telefono}, Mail: {mail}\n")
 opcion = input("¿Deseas agregar otro registro? (s/n): ")
    if opcion.lower() != "s":
    break
archivo.close()

