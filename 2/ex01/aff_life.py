from load_csv import load, personal_timer
import plotly.express as px
import pandas as pd


def prepare_data(data: pd.DataFrame):
    """
    changes the data from horizontal to vertical
    """
    df_long = data.melt(
        id_vars=["country"], var_name="Year", value_name="Life Expectancy"
    )
    df_long["Year"] = df_long["Year"].astype(int)
    return df_long


def show_interactive_countries(data: pd.DataFrame):
    """
    creates the figure with the prepared data
    """
    df_long = prepare_data(data)

    fig = px.line(
        df_long,
        x="Year",
        y="Life Expectancy",
        color="country",  # makes the line, called trace
        title="World Life Expectancy",
        template="plotly_dark",
    )
    fig.update_traces(hovertemplate="<b>%{y:.1f} years</b><br>Year: %{x}")

    # hides all traces and makes Germany visible
    fig.for_each_trace(lambda trace: trace.update(visible=False))
    fig.for_each_trace(
        lambda trace: (trace.update(visible=True) if trace.name == "Germany" else None)
    )

    fig.write_html("result_ex00.html")
    print("Wrote result to file")


def main():
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            raise Exception("no data in file or file non existant")
    except Exception as e:
        print(f"Error: {e}")
        return 1

    show_interactive_countries(data)

    return 0


if __name__ == "__main__":
    main()
