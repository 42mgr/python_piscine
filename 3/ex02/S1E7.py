from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __str__(self) -> str:
        """__str__ overrride"""
        return f"Vector: ({self.familiy_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """__repr__ overrride"""
        return f"Vector: ({self.familiy_name}, {self.eyes}, {self.hairs})"

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """init for Baratheon"""
        super().__init__(first_name, is_alive)
        self.familiy_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Bartheon familiy member dies"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister familiy."""

    def __str__(self) -> str:
        """__str__ override"""
        return f"Vector: ({self.familiy_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """__repr__ overrride"""
        return f"Vector: ({self.familiy_name}, {self.eyes}, {self.hairs})"

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """init for Lannister"""
        super().__init__(first_name, is_alive)
        self.familiy_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """class Lannister die function"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True) -> Character:
        """creates a new lannister object"""
        new_lannister = cls(first_name, is_alive)
        return new_lannister


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(
            f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}"
        )

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
