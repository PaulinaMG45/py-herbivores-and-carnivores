class Animal:
    alive = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        # Register every created animal
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:

        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive = [
                animal
                for animal in Animal.alive
                if animal != herbivore
            ]


# Only for manual testing
if __name__ == "__main__":

    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")

    print(Animal.alive)
