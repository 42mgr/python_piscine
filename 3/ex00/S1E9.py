from abc import ABC, abstractmethod


class Character(ABC):
    """
    abstract class implementation
    """

    def __str__(self) -> str:
        return f"Vector: ({self.first_name},)"

    def __init__(self, first_name: str, is_alive=True) -> None:
        """docstring of init in abstract class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """docstring of die in abstract class"""
        pass


class Stark(Character):
    """class Stark: implements the abstract class"""

    def die(self) -> None:
        """docstring of die in class Stark"""
        self.is_alive = False


def main():
    """
    has the tester from the exercise
    does the error handling
    """
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        hodor = Character("hodor")
    except TypeError as e:
        print(f"TypeError: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
