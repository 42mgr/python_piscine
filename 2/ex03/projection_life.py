from load_csv import load
import pandas as pd
import plotly.express as px


def convert_to_number(value) -> float:
    """
    32m in the csv mean 32_000,
    therefore all numbers need to be checked and converted
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


def prepare_data(data: pd.DataFrame, col_name: str):
    """
    the data is in columns in the csv and need to be changed to a single column
    """
    df_long = data.melt(id_vars=["country"], var_name="Year", value_name=col_name)
    df_long["Year"] = df_long["Year"].astype(int)
    df_long[col_name] = df_long[col_name].apply(convert_to_number)
    return df_long


def merge_data(life_df, gdp_df, pop_df):
    """
    the different dataframes get merged on country and year
    """
    life_long = prepare_data(life_df, "life_expectancy")
    gdp_long = prepare_data(gdp_df, "gdp")
    pop_long = prepare_data(pop_df, "population")

    merged = pd.merge(life_long, gdp_long, on=["country", "Year"])
    merged = pd.merge(merged, pop_long, on=["country", "Year"])

    merged = merged.dropna()

    return merged


def show_gapminder(merged_df):
    """
    gapminder.org is the idea behind this visualization
    shows all the years from 1900-1950 (hardware limitation)
    each country is a bubble with the population size
    vertically is the life_expectancy
    horizontally the gdp (log)
    """

    fig = px.scatter(
        merged_df,
        x="gdp",
        y="life_expectancy",
        animation_frame="Year",  # the slider is connected to the year
        animation_group="country",  # follow the country bubble over the year
        size="population",
        color="country",
        hover_name="country",
        log_x=True,
        size_max=80,  # china would make everyone disappear
        range_x=[300, 100_000],  # gdp
        range_y=[0, 110],  # age
        title="Life Expectancy vs. GDP and Population Size (1900 - 1950)",
        template="plotly_dark",
    )

    fig.write_html("result_ex03.html")
    print("Result written to file.")


def main():
    # read the df
    life_df = load("life_expectancy_years.csv")
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    pop_df = load("population_total.csv")

    # merge and prepare the df
    merged_df = merge_data(life_df, gdp_df, pop_df)
    merged_df = merged_df[merged_df["Year"].between(1900, 1950)]

    # max_row_index = merged_df["gdp"].idxmax()
    # print("--- Record with Highest GDP ---")
    # print(merged_df.loc[max_row_index])

    show_gapminder(merged_df)


if __name__ == "__main__":
    main()
