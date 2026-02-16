import pandas as pd
from .config import RAW_DATA

def load_matches() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupMatches.csv")

def load_players() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupPlayers.csv")

def load_scorers() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "GoalScorers.csv")
