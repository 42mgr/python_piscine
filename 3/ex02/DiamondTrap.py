from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """I'm a king now"""

    def __init__(self, first_name: str):
        """makes sure only one ABC is initiated"""
        super().__init__(first_name, True)

    def set_eyes(self, color: str):
        """eyes setter method"""
        self.eyes = color

    def get_eyes(self) -> str:
        """eyes getter method"""
        return f"{self.eyes}"

    def set_hairs(self, color: str):
        """hairs setter method"""
        self.hairs = color

    def get_hairs(self) -> str:
        """hairs getter method"""
        return f"{self.hairs}"


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)

        Napoleon = King("Napoleon")
        Napoleon.familiy_name = "Napoleon"
        print(Napoleon)

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
