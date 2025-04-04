class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if person in self.passengers:
            print(f"{person.name} ya está en el bus.")
            return
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} ha subido al bus.")
        else:
            print("El bus está lleno. No se pueden agregar más pasajeros.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} ha bajado del bus.")
        else:
            print(f"{person.name} no está en el bus.")


# Ejemplo de clase Person para referencia:
class Person:
    def __init__(self, name):
        self.name = name


def main():
    # Crear una instancia de Bus con un máximo de 3 pasajeros
    bus = Bus(max_passengers=3)

    # Crear algunas instancias de Person
    person1 = Person(name="Juan")
    person2 = Person(name="Maria")
    person3 = Person(name="Carlos")
    person4 = Person(name="Ana")

    # Agregar pasajeros al bus
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.add_passenger(person3)

    # Intentar agregar un pasajero adicional
    bus.add_passenger(person4)

    # Remover un pasajero del bus
    bus.remove_passenger(person2)

    # Intentar remover un pasajero que no está en el bus
    bus.remove_passenger(person4)


if __name__ == "__main__":
    main()
