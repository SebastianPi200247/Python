def mayor_que_20(peso, altura, edad):
    if type(peso) == int and type(altura) == int and type(edad) == int:
       suma = (peso + altura + edad)         
       print(suma, type(suma))            
    else:
        raise Exception('no es un numero')
        
    if (suma)>20:
        return str(suma) 
    else:
        return False                         
try:    
    resultado = mayor_que_20(1,2,3) 
    print ('respuesta', resultado)
except Exception:
    print ('no funciona')    

def mayor_que_20(peso, altura, edad):
    if type(peso) == int and type(altura) == int and type(edad) == int:
       suma = (peso + altura + edad)         
       print(suma, type(suma))            
    else:
         raise Exception('no son numeros')
    if (suma)>20:
        return str(suma) 
    else:
        return False                         
try:

    resultado = mayor_que_20(1,2,30) 
    print ('respuesta', resultado)
except Exception:
    print ('no funca')    

def mayor_que_20(peso, altura, edad):
    if type(peso) == int and type(altura) == int and type(edad) == int:
       suma = (peso + altura + edad)         
       print(suma, type(suma))            
    else:
        raise Exception('No juega eso')
    if (suma)>20:
        return str(suma) 
    else:
        return False                         
try:
    resultado = mayor_que_20(1,2,"hola") 
    print ('respuesta', resultado)
except Exception as c :
    print (c) 
    

def mayor_que_20_lista(lista):
    if lista[0] is int and lista[1] is int and lista[2] is str:
       suma = (lista[0] + lista[1] + lista[2])   
       print(lista)            
    else:
        return None
    if (suma)>20:
        return str(suma) 
    else:
        return False                         

resultado = mayor_que_20_lista([1,2,"hola"]) 
print ('respuesta', resultado)


def mayor_que_20_tuplas(tupla):
    peso = tupla[0]
    altura = tupla[1]
    edad = tupla[2]
    if type(peso) is int and type(altura) is int and type (edad) is int:
       suma = (peso + altura + edad)         
       print(suma, type(suma))            
    else:
        return None
    if (suma)>20:
        return str(suma) 
    else:
        return False                         
resultado = mayor_que_20_tuplas((1, 2, 30)) 
print ('respuesta', resultado)

