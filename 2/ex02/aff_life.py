from load_csv import load, personal_timer
import plotly.express as px
import pandas as pd


def convert_to_number(value) -> float:
    """
    if number is non numeric, e.g. 30k it is
    converted to 30_000
    """
    if isinstance(value, (int, float)):
        return float(value)

    value = str(value).lower().replace(",", "")

    if "k" in value:
        return float(value.replace("k", "")) * 1_000
    if "m" in value:
        return float(value.replace("m", "")) * 1_000_000
    if "b" in value:
        return float(value.replace("b", "")) * 1_000_000_000

    return float(value)


def prepare_data(data: pd.DataFrame):
    """
    converts everything from vertical to horizontal layout
    """
    df_long = data.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="Population Projections",
    )
    df_long["Year"] = df_long["Year"].astype(int)

    df_long["Population Projections"] = df_long["Population Projections"].apply(
        convert_to_number
    )
    return df_long


@personal_timer
def show_interactive_countries(data: pd.DataFrame):
    """
    creates the figure with long df
    similar to previous exercise but now all countries can be shown
    """
    df_long = prepare_data(data)

    fig = px.line(
        df_long,
        x="Year",
        y="Population Projections",
        color="country",  # makes the traces
        title="Poplulation Projections",
        template="plotly_dark",
    )

    fig.update_traces(hovertemplate="<b>Population %{y:.2s}</b><br>Year: %{x}")

    fig.for_each_trace(lambda trace: trace.update(visible="legendonly"))
    fig.for_each_trace(
        lambda trace: (trace.update(visible=True) if trace.name == "Germany" else None)
    )
    fig.for_each_trace(
        lambda trace: (trace.update(visible=True) if trace.name == "France" else None)
    )
    # fig.update_yaxes(range=[0, 100])
    fig.update_xaxes(tickmode="auto", nticks=12, maxallowed=2050)
    fig.update_yaxes(range=[0, None])
    fig.write_html("result_ex02.html")
    print("Result written to file")


def main():
    try:
        data = load("population_total.csv")
        if data is None:
            raise Exception("no data in file or file non existant")
    except Exception as e:
        print(f"Error: {e}")
        return 1

    show_interactive_countries(data)

    return 0


if __name__ == "__main__":
    main()
