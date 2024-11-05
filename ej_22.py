#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#e el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from cola import Queue

def obtener_nombre_personaje_superheroe(cola, superheroe):
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        personaje = cola.attention()
        if personaje["nombre_superheroe"] == superheroe:
            return personaje["nombre_personaje"]
        cola.move_to_end()
    return None

def mostrar_superheroes_femeninos(cola):
    print("Superhéroes femeninos:")
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        personaje = cola.attention()
        if personaje["genero"] == "Femenino":
            print(personaje["nombre_superheroe"])
        cola.move_to_end()

def mostrar_personajes_masculinos(cola):
    print("Personajes masculinos:")
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        personaje = cola.attention()
        if personaje["genero"] == "Masculino":
            print(personaje["nombre_personaje"])
        cola.move_to_end()

def obtener_superheroe_por_personaje(cola, personaje):
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        heroe = cola.attention()
        if heroe["nombre_personaje"] == personaje:
            return heroe["nombre_superheroe"]
        cola.move_to_end()
    return None

def mostrar_datos_personajes_con_letra(cola, letra):
    print(f"Datos de los superhéroes/personajes cuyos nombres comienzan con '{letra}':")
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        personaje = cola.attention()
        if personaje["nombre_personaje"].startswith(letra.upper()) or personaje["nombre_superheroe"].startswith(letra.upper()):
            print(personaje)
        cola.move_to_end()

def verificar_existencia_personaje(cola, personaje):
    tamano_cola = cola.size()
    for _ in range(tamano_cola):
        heroe = cola.attention()
        if heroe["nombre_personaje"] == personaje:
            print(f"El personaje {personaje} se encuentra en la cola, su nombre de superhéroe es {heroe['nombre_superheroe']}")
            return True
        cola.move_to_end()
    print(f"El personaje {personaje} no se encuentra en la cola.")
    return False

# Crear cola de personajes de Marvel
cola_personajes = Queue()
cola_personajes.arrive({"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Capitana Marvel", "genero": "Femenino"})
cola_personajes.arrive({"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "Femenino"})
cola_personajes.arrive({"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "Masculino"})
cola_personajes.arrive({"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "Masculino"})
cola_personajes.arrive({"nombre_personaje": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "Masculino"})
cola_personajes.arrive({"nombre_personaje": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "Masculino"})

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_capitana_marvel = obtener_nombre_personaje_superheroe(cola_personajes, "Capitana Marvel")
print(f"El nombre del personaje de la superhéroe Capitana Marvel es: {nombre_capitana_marvel}")

# b. Mostrar los nombre de los superhéroes femeninos
mostrar_superheroes_femeninos(cola_personajes)

# c. Mostrar los nombres de los personajes masculinos
mostrar_personajes_masculinos(cola_personajes)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
nombre_superheroe_scott_lang = obtener_superheroe_por_personaje(cola_personajes, "Scott Lang")
print(f"El superhéroe del personaje Scott Lang es: {nombre_superheroe_scott_lang}")

# e. Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S
mostrar_datos_personajes_con_letra(cola_personajes, "S")

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes
verificar_existencia_personaje(cola_personajes, "Carol Danvers")
