# Zaprojektuj i wykonaj klasy reprezentujące przedmiot o masie podanej w
# kilogramach oraz pojemnik (który sam jest przedmiotem) o podanym udźwigu.
# Przedmioty można wkładać i wyjmować z pojemników, o ile są one w ramach
# dopuszczalnego udźwigu (w przeciwnym razie nie udaje się włożyć przedmiotu do
# pojemnika). Program ma umożliwić wypisanie zawartości każdego pojemnika w
# postaci zestawu mas przedmiotów, które się w nim znajdują.


class OverCargoLimit(Exception):
    def __init__(self) -> None:
        super().__init__("Chosen item will overfill container")


class Item:
    """
    Item object having own mass
    """

    def __init__(self, mass) -> None:
        self._mass = mass


class Container(Item):
    """
    container Item having capacity
    """

    def __init__(self, mass, capacity) -> None:
        super().__init__(mass)
        self._capacity = capacity
        self._inside = {}

    def put_in(self, inserted: Item):
        if isinstance(inserted, Item):
            if sum(self._inside.values()) + inserted._mass <= self._capacity:
                self._inside[inserted] = inserted._mass
                self._mass += sum(self._inside.values())
            else:
                raise (OverCargoLimit)


if __name__ == "__main__":
    Kijek = Item(5)
    Oko = Item(20)
    Plecak = Container(1, 15)
    Auto = Container(25, 100)

    print(Kijek._mass)
    print(Plecak._mass)
    Plecak.put_in(Kijek)
    print(Plecak._mass)
