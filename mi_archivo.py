nombre = "Juan".upper()
otra_variable  = nombre
print(f"hola, soy {nombre}")

# Holi, soy un comentario feliz :)
# snake case
# Inferencia de tipos
# Negociacion o trade-off
mi_numero_1 = 500
mi_numero_2 = 500
sinNombre = None # null
meGustaElPolloFrito = False # false

#print(type(str(mi_numero_1)))

# camel case
miNumer3 = 1000
print(1+1)
#print(mi_numero_1 + mi_numero_2 - miNumer3)

edad1= 18
edad2= 10

if edad1 > edad2:
    print("edad1 es mayor")
    if edad2 == edad1:
        print("es igual")
        
persona = {
    "nombre": "Pepe"
    , "edad":16
}

persona1 = {
    "nombre": "Pepito"
    , "edad":11
}

lista_personas = [persona, persona1]

print(lista_personas)

# funciones
def mifuncion():
    return "Holi, soy una funcion"

def mifuncion_2(nombre):
    return f"Holi, soy una {nombre}"

#print(mifuncion_2('manzana'))