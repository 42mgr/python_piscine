import sys
import ast


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    returns a list of the BMIs for the provided lists
    and raises errors if necessary
    """
    if len(height) != len(weight):
        raise ValueError("unequal lengths of height and weight list input")
    if any(x == 0 for x in height + weight):
        raise ValueError("entry with invalid value '0' in input")
    try:
        float_height = [float(x) for x in height]
        float_weight = [float(x) for x in weight]
    except (ValueError, TypeError):
        raise ValueError("list elements must be numbers")
    if not all(x > 0 for x in float_weight + float_height):
        raise ValueError("values must be all greater 0")

    return [round(w / (h**2), 2) for w, h in zip(float_weight, float_height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    compares a list of BMIs to a provided limit
    returns a list of boolean
    """
    return [x > limit for x in bmi]


def do_bmi_calculation(height: list[int | float], weight: list[int | float]):
    """
    here the bmi is calculated and printed
    bmi limit is asked and applied in print
    """
    bmi = give_bmi(height, weight)
    limit = int(input("What is the bmi limit? "))
    print("")
    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))


def main():
    """
    regular main to easier testing
    """
    args = sys.argv[1:]

    try:
        # transform args into valid python data structure (tuples, list, etc)
        list_args = [ast.literal_eval(arg) for arg in args]
    except (ValueError, SyntaxError):
        print("ValueError: Arguments must be valid lists")
        return 1

    try:
        match list_args:
            # verify if user input was two lists
            case [list() as height, list() as weight] if all(
                isinstance(x, (int, float)) for x in height + weight
            ):
                do_bmi_calculation(height, weight)

            case []:
                height = [2.71, 1.15]
                weight = [165.3, 38.4]
                print(
                    f"No user input. Tester values will be used: \n"
                    f"height = {height} \nweight = {weight}"
                )
                do_bmi_calculation(height, weight)
            case _:
                raise ValueError("invalid input")
    except ValueError as e:
        print("ValueError:", e)
        return 1
    except Exception as e:
        print("Error:", e)

    return 0


if __name__ == "__main__":
    sys.exit(main())
