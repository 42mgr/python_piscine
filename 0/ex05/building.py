import sys


def print_results(results: dict):
    """
    - prints the result dictionary
    - ensures that a value 0 is provided if key is missing
    - adds "s" for plural
    """

    def s(count):
        """
        simple helper function for plural
        """
        return "s" if count != 1 else ""

    total = results.get("total", 0)
    upper = results.get("upper", 0)
    lower = results.get("lower", 0)
    punct = results.get("punctuation", 0)
    space = results.get("spaces", 0)
    digit = results.get("digits", 0)

    output = f"""The text contains {total} character{s(total)}:
{upper} upper letter{s(upper)}
{lower} lower letter{s(lower)}
{punct} punctuation mark{s(punct)}
{space} space{s(space)}
{digit} digit{s(digit)}"""
    print(output)


def count(text: str) -> None:
    """
    - takes string and does the counting
    - category is only created if case matched
    """
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    results = {"total": len(text)}

    for character in text:
        match character:
            case c if c.islower():
                category = "lower"
            case c if c.isupper():
                category = "upper"
            case c if c.isdigit():
                category = "digits"
            case c if c.isspace():
                category = "spaces"
            case c if c in punctuations:
                category = "punctuation"
            case _:
                category = "other"
        results[category] = results.get(category, 0) + 1

    print_results(results)


def main():
    """
    - checks for the input, match case []
    - uses readline() instead of input() to count carriage returns
    - handles Crtl+C Crtl+D keyboardInterrupts
    """
    args = sys.argv[1:]

    try:
        buffer = ""
        match args:
            case []:
                # buffer = input("What is the text to count?\n")
                # if Ctrl+D is used on "" I get a traceback
                print("What is the the text to count?")
                buffer = sys.stdin.readline()
            case [text]:
                buffer = text
            case _:
                assert len(args) <= 1, "more than one argument is provided"

    except AssertionError as error:
        print("AssertionError:", error)
        return 1

    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled by user.")
        return 1

    count(buffer)

    return 0


if __name__ == "__main__":
    sys.exit(main())
