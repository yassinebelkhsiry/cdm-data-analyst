import pandas as pd
import numpy as np

def worldcup_summary(matches: pd.DataFrame, teams: pd.DataFrame) -> pd.DataFrame:
    # teams = output of teams_per_year()
    s = (
        matches.groupby("year")
               .agg(
                   matches=("matchid", "nunique"),
                   total_goals=("total_goals", "sum"),
                   goals_per_match=("total_goals", "mean"),
                   avg_attendance=("attendance", "mean"),
                   total_attendance=("attendance", "sum"),
               )
               .reset_index()
    )
    s = s.merge(teams, on="year", how="left")
    return s.sort_values("year").reset_index(drop=True)

def compare_years(summary: pd.DataFrame, y1: int, y2: int) -> pd.DataFrame:
    years = [y for y in [y1, y2] if y in summary["year"].values]
    return summary[summary["year"].isin(years)].copy()

def top_scorers_latest(scorers: pd.DataFrame, year: int, top_n: int = 10) -> pd.DataFrame:
    s = scorers.copy()
    s = s[s["year"] == year].sort_values("number_of_goals", ascending=False)
    return s.head(top_n)

def trend_slope_goals_per_match(summary: pd.DataFrame) -> float:
    df = summary.dropna(subset=["year", "goals_per_match"]).copy()
    x = df["year"].astype(float).values
    y = df["goals_per_match"].astype(float).values
    if len(x) < 3:
        return float("nan")
    return float(np.polyfit(x, y, 1)[0])
