
contactos = {}

while True :
    
    nombre = input("Ingrese el nombre: ")
    cel = input("Ingrese su cel:")
    edad = input ("Ingrese su edad:")
   
    contactos[nombre] = (cel,edad)
    
    print("Nombres: ", contactos)
    set keys = contactos.keyset();