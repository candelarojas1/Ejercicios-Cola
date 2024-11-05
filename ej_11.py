
from cola import Queue 

# Crear la cola con los personajes de Star Wars y sus planetas de origen
star_wars_queue = Queue()
star_wars_queue.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
star_wars_queue.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
star_wars_queue.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
star_wars_queue.arrive({"nombre": "Yoda", "planeta": "Desconocido"})
star_wars_queue.arrive({"nombre": "Chewbacca", "planeta": "Kashyyyk"})
star_wars_queue.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
star_wars_queue.arrive({"nombre": "Darth Vader", "planeta": "Tatooine"})

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_personajes_por_planeta(planeta):
    personajes = []
    for _ in range(star_wars_queue.size()):
        personaje = star_wars_queue.attention()
        if personaje["planeta"] == planeta:
            personajes.append(personaje["nombre"])
        star_wars_queue.move_to_end()
    return personajes

personajes_alderaan = mostrar_personajes_por_planeta("Alderaan")
personajes_endor = mostrar_personajes_por_planeta("Endor")
personajes_tatooine = mostrar_personajes_por_planeta("Tatooine")

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def planeta_natal(nombre_personaje):
    for _ in range(star_wars_queue.size()):
        personaje = star_wars_queue.attention()
        if personaje["nombre"] == nombre_personaje:
            planeta = personaje["planeta"]
            star_wars_queue.move_to_end()
            return planeta
        star_wars_queue.move_to_end()

planeta_luke = planeta_natal("Luke Skywalker")
planeta_han = planeta_natal("Han Solo")

# c. Insertar un nuevo personaje antes del maestro Yoda
nuevo_personaje = {"nombre": "Obi-Wan Kenobi", "planeta": "Desconocido"}
for _ in range(star_wars_queue.size()):
    personaje = star_wars_queue.attention()
    if personaje["nombre"] == "Yoda":
        star_wars_queue.arrive(nuevo_personaje)
    star_wars_queue.move_to_end()

# d. Eliminar el personaje ubicado después de Jar Jar Binks
for _ in range(star_wars_queue.size()):
    personaje = star_wars_queue.attention()
    if personaje["nombre"] == "Jar Jar Binks":
        star_wars_queue.attention()  # Eliminar el siguiente personaje
    else:
        star_wars_queue.move_to_end()

# Mostrar los resultados
print("a. Personajes del planeta Alderaan:", personajes_alderaan)
print("   Personajes del planeta Endor:", personajes_endor)
print("   Personajes del planeta Tatooine:", personajes_tatooine)
print("b. Planeta natal de Luke Skywalker:", planeta_luke)
print("   Planeta natal de Han Solo:", planeta_han)
