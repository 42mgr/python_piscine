class calculator:
    """claculator implementation"""

    def __init__(self, lst: list):
        """init calc"""
        self.lst = lst

    def __add__(self, object) -> None:
        """add calc"""
        print([item + object for item in self.lst])

    def __mul__(self, object) -> None:
        """multiply calc"""
        print([item * object for item in self.lst])

    def __sub__(self, object) -> None:
        """substract calc"""
        print([item - object for item in self.lst])

    def __truediv__(self, object) -> None:
        """divide calc"""
        try:
            print([item / object for item in self.lst])
        except Exception as e:
            print(f"Error: {e}")


def Print(input: str):
    print(f"{input}")


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    Print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    Print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    # wrong input in excercise
    v3 = calculator([5.0, 10.0, 15.0])
    v3 - 5
    v3 / 5
    Print("--- div by 0 ---")
    v3 / 0
    return 0


if __name__ == "__main__":
    main()
