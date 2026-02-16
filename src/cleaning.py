import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
          .str.strip()
          .str.lower()
          .str.replace(r"[^\w]+", "_", regex=True)
          .str.replace(r"_+", "_", regex=True)
          .str.strip("_")
    )
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().copy()

def clean_matches(matches: pd.DataFrame) -> pd.DataFrame:
    m = standardize_columns(matches)

    # types
    for col in ["year", "roundid", "matchid"]:
        if col in m.columns:
            m[col] = pd.to_numeric(m[col], errors="coerce").astype("Int64")

    for col in ["home_team_goals", "away_team_goals", "attendance"]:
        if col in m.columns:
            m[col] = pd.to_numeric(m[col], errors="coerce")

    if "datetime" in m.columns:
        m["datetime"] = pd.to_datetime(m["datetime"], errors="coerce")

    # features
    if "home_team_goals" in m.columns and "away_team_goals" in m.columns:
        m["total_goals"] = m["home_team_goals"].fillna(0) + m["away_team_goals"].fillna(0)

    return drop_duplicates(m)

def clean_players(players: pd.DataFrame) -> pd.DataFrame:
    p = standardize_columns(players)
    for col in ["year", "roundid", "matchid", "shirt_number"]:
        if col in p.columns:
            p[col] = pd.to_numeric(p[col], errors="coerce").astype("Int64")
    return drop_duplicates(p)

def clean_scorers(scorers: pd.DataFrame) -> pd.DataFrame:
    s = standardize_columns(scorers)

    # some datasets name it "player_s"
    if "player_s" in s.columns and "player" not in s.columns:
        s = s.rename(columns={"player_s": "player"})

    for col in ["year", "number_of_goals"]:
        if col in s.columns:
            s[col] = pd.to_numeric(s[col], errors="coerce").astype("Int64")

    return drop_duplicates(s)
