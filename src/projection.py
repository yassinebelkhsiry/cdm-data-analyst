import pandas as pd

def projection_2026(summary: pd.DataFrame, expected_matches: int = 104, expected_teams: int = 48, last_n: int = 5) -> dict:
    recent = summary.sort_values("year").tail(last_n)
    gpm = float(recent["goals_per_match"].mean())

    est_total_goals = gpm * expected_matches
    est_goals_per_team = est_total_goals / expected_teams

    return {
        "year": 2026,
        "expected_matches": expected_matches,
        "expected_teams": expected_teams,
        "estimated_goals_per_match": gpm,
        "estimated_total_goals": float(est_total_goals),
        "estimated_goals_per_team": float(est_goals_per_team),
    }
