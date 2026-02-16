import matplotlib.pyplot as plt
import pandas as pd

def plot_goals_per_match(summary: pd.DataFrame):
    plt.figure()
    plt.plot(summary["year"], summary["goals_per_match"])
    plt.title("Goals per Match Evolution")
    plt.xlabel("Year")
    plt.ylabel("Goals per Match")
    plt.show()

def plot_matches(summary: pd.DataFrame):
    plt.figure()
    plt.plot(summary["year"], summary["matches"])
    plt.title("Matches per World Cup")
    plt.xlabel("Year")
    plt.ylabel("Matches")
    plt.show()

def bar_goals_compare(summary_two_years: pd.DataFrame):
    plt.figure()
    plt.bar(summary_two_years["year"].astype(str), summary_two_years["total_goals"])
    plt.title("Total Goals Comparison")
    plt.xlabel("Year")
    plt.ylabel("Total Goals")
    plt.show()
