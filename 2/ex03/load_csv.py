import pandas as pd
from pandas.errors import EmptyDataError, ParserError
import datetime


def personal_timer(function):
    """
    exercise: wraps the function call within a timer function
    """

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = function(*args, **kwargs)
        duration = datetime.datetime.now() - start_time
        print(f"Duration: {duration}")
        return result

    return wrapper


@personal_timer
def load(path: str) -> pd.DataFrame | None:
    """
    loads a csv
    prints dimensions
    returns panda dataframe
    """
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions: ", df.shape)
        return df

    except FileNotFoundError as e:
        print(f"{FileNotFoundError.__name__}: {e}")
        return None
    except pd.errors.EmptyDataError as e:
        print(f"{EmptyDataError.__name__}: {e}")
        return None
    except pd.errors.ParserError as e:
        print(f"{ParserError.__name__}: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # print(load("quatsch"))
    # print(load("test.csv"))
    # print(load("test"))
    print(load("population_total.csv"))
