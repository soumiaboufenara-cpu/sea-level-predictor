import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Extend line to 2050
    years = pd.Series(range(1880, 2051))

    ax.plot(
        years,
        slope * years + intercept,
        label="Line of best fit"
    )

    # Second line of best fit using data from 2000
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Extend second line to 2050
    years_recent = pd.Series(range(2000, 2051))

    ax.plot(
        years_recent,
        slope_recent * years_recent + intercept_recent,
        label="Line of best fit since 2000"
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return plot
    fig.savefig("sea_level_plot.png")

    return fig
