import pandas as pd

def teams_per_year(matches: pd.DataFrame) -> pd.DataFrame:
    # expects columns: year, home_team_name, away_team_name
    home = matches[["year", "home_team_name"]].rename(columns={"home_team_name": "team"})
    away = matches[["year", "away_team_name"]].rename(columns={"away_team_name": "team"})

    out = (
        pd.concat([home, away], ignore_index=True)
          .dropna()
          .drop_duplicates()
          .groupby("year")["team"].nunique()
          .reset_index(name="teams")
    )
    return out

def add_goal_diff(matches: pd.DataFrame) -> pd.DataFrame:
    m = matches.copy()
    if "home_team_goals" in m.columns and "away_team_goals" in m.columns:
        m["goal_diff"] = (m["home_team_goals"] - m["away_team_goals"]).abs()
    return m
