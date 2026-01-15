import sys

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def create_morse(text: str) -> str:
    """
    Takes string and converts it into a morse string.
    """
    # Validation
    if not all(char.upper() in MORSE_CODE_DICT for char in text):
        raise AssertionError
    # Create morse
    # print(f"DEBUG: {text.split()=}")
    return " ".join(MORSE_CODE_DICT[char.upper()] for char in text)


def decode_morse(morse: str) -> str:
    """
    Exercise decoder for morse
    """
    DECODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
    return "".join(DECODE_DICT[char] for char in morse.split())


def main():
    """
    Takes only one argument
    """
    args = sys.argv[1:]

    try:
        match args:
            case [text]:
                morse_text = create_morse(text)
                print(morse_text)
                # print(decode_morse(morse_text))
                return 0
            case _:
                raise AssertionError

    except AssertionError:
        print("AssertionError: the arguments are bad")
        return 1


if __name__ == "__main__":
    sys.exit(main())
