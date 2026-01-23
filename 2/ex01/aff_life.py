from load_csv import load, personal_timer
import plotly.express as px
import pandas as pd

# crtl o und crtl i!!!!


def prepare_data(data: pd.DataFrame):
    df_long = data.melt(
        id_vars=["country"], var_name="Year", value_name="Life Expectancy"
    )
    df_long["Year"] = df_long["Year"].astype(int)
    return df_long


def show_interactive_countries(data: pd.DataFrame):
    df_long = prepare_data(data)

    # 2. Plot
    fig = px.line(
        df_long,
        x="Year",
        y="Life Expectancy",
        color="country",  # <--- This creates the lines and the list!
        title="World Life Expectancy",
        template="plotly_dark",
    )

    # 3. Clean up the hover labels explicitly (optional, but good practice)
    fig.update_traces(hovertemplate="<b>%{y:.1f} years</b><br>Year: %{x}")
    # Hide everyone initially...
    fig.for_each_trace(lambda trace: trace.update(visible=False))

    # ...except Germany (make sure the string matches your CSV exactly!)
    fig.for_each_trace(
        lambda trace: (
            trace.update(visible=True) if trace.name == "Germany" else None
        )
    )
    fig.show()


@personal_timer
def show_country(data: pd.DataFrame, country: str):
    country_data = data[data["country"] == country]
    if country_data.empty:
        print(f"Country not found: {country}")
        return
    country_data = country_data.drop(columns=["country"])

    fig = px.line(
        x=country_data.columns,
        y=country_data.values[0],
        title=f"Life Expectancy: {country}",
        markers=True,
        template="plotly_dark",
    )

    fig.update_layout(xaxis_title="Year", yaxis_title="Life Expectancy")
    fig.update_yaxes(range=[0, 100])
    fig.update_xaxes(tickmode="auto", nticks=12)
    fig.show()


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
