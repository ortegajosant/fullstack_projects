class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if person in self.passengers:
            print(f"{person.name} is already on the bus.")
            return
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus.")
        else:
            print("The bus is full. No more passengers can be added.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has left the bus.")
        else:
            print(f"{person.name} is not on the bus.")


# Example of a Person class for reference:
class Person:
    def __init__(self, name):
        self.name = name


def main():
    # Create an instance of Bus with a maximum of 3 passengers
    bus = Bus(max_passengers=3)

    # Crear algunas instancias de Person
    person1 = Person(name="Juan")
    person2 = Person(name="Maria")
    person3 = Person(name="Carlos")
    person4 = Person(name="Ana")

    # Add passengers to the bus
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.add_passenger(person3)

    # Try to add an additional passenger
    bus.add_passenger(person4)

    # Remove a passenger from the bus
    bus.remove_passenger(person2)

    # Try to remove a passenger who is not on the bus
    bus.remove_passenger(person4)


if __name__ == "__main__":
    main()
