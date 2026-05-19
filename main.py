from pathlib import Path

import pandas as pd
import streamlit as st


APP_TITLE = "CDM Data Analyst"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "processed"
HERO_IMAGE = (
    "https://images.unsplash.com/photo-1579952363873-27f3bade9f55"
    "?auto=format&fit=crop&w=1600&q=80"
)
VISUALS = [
    {
        "title": "Tournament atmosphere",
        "url": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=900&q=80",
    },
    {
        "title": "Match intensity",
        "url": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&w=900&q=80",
    },
    {
        "title": "Data storytelling",
        "url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=80",
    },
]


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        :root {
            --brand-red: #c8102e;
            --brand-blue: #0b3d91;
            --ink: #102033;
            --muted: #667085;
            --panel: rgba(255, 255, 255, 0.92);
            --line: rgba(16, 32, 51, 0.10);
        }

        .stApp {
            background:
                linear-gradient(180deg, rgba(248, 250, 252, 0.96), rgba(241, 245, 249, 1)),
                #f8fafc;
            color: var(--ink);
        }

        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--line);
        }

        .hero {
            min-height: 310px;
            border-radius: 0;
            overflow: hidden;
            background:
                linear-gradient(90deg, rgba(5, 16, 33, 0.88), rgba(5, 16, 33, 0.48)),
                url("__HERO_IMAGE__");
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: flex-end;
            padding: 42px;
            margin: -2.8rem -3.2rem 2rem -3.2rem;
        }

        .hero h1 {
            color: #ffffff;
            font-size: clamp(2.2rem, 5vw, 4.4rem);
            line-height: 1;
            margin: 0 0 0.65rem;
            letter-spacing: 0;
        }

        .hero p {
            color: rgba(255, 255, 255, 0.86);
            max-width: 760px;
            font-size: 1.05rem;
            margin: 0;
        }

        .section-kicker {
            color: var(--brand-red);
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.35rem;
        }

        .metric-card {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 18px 18px 16px;
            min-height: 118px;
            box-shadow: 0 12px 30px rgba(16, 32, 51, 0.06);
        }

        .metric-card span {
            color: var(--muted);
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .metric-card strong {
            display: block;
            color: var(--ink);
            font-size: 2rem;
            line-height: 1.15;
            margin-top: 0.55rem;
        }

        .metric-card small {
            color: var(--muted);
        }

        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 16px;
        }

        .block-container {
            padding-top: 2.8rem;
            padding-bottom: 3rem;
        }
    </style>
    """.replace("__HERO_IMAGE__", HERO_IMAGE),
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    required_files = {
        "matches": DATA_DIR / "matches_clean.csv",
        "kpi": DATA_DIR / "kpi_worldcup.csv",
        "projection": DATA_DIR / "projection_2026.csv",
    }
    missing = [str(path.relative_to(BASE_DIR)) for path in required_files.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing processed data files: " + ", ".join(missing))

    matches = pd.read_csv(required_files["matches"], parse_dates=["datetime"])
    kpi = pd.read_csv(required_files["kpi"])
    projection = pd.read_csv(required_files["projection"])
    return matches, kpi, projection


def compact_number(value: float | int | None) -> str:
    if pd.isna(value):
        return "N/A"
    value = float(value)
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:,.0f}"


def metric_card(label: str, value: str, caption: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <span>{label}</span>
            <strong>{value}</strong>
            <small>{caption}</small>
        </div>
        """,
        unsafe_allow_html=True,
    )


try:
    matches, kpi, projection = load_data()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()


all_years = sorted(kpi["year"].dropna().astype(int).unique())

with st.sidebar:
    st.title("World Cup Lab")
    st.caption("Analyse FIFA World Cup 1930-2022 avec projection 2026.")
    selected_years = st.multiselect(
        "Editions",
        all_years,
        default=all_years,
        help="Filtre les KPIs, graphiques et matchs affiches.",
    )
    min_attendance = int(matches["attendance"].dropna().min()) if matches["attendance"].notna().any() else 0
    max_attendance = int(matches["attendance"].dropna().max()) if matches["attendance"].notna().any() else 0
    attendance_range = st.slider(
        "Attendance",
        min_value=min_attendance,
        max_value=max_attendance,
        value=(min_attendance, max_attendance),
        step=1000,
    )
    st.divider()
    st.caption("Portfolio Data Analyst - Yassine Belkhsiry")


if not selected_years:
    st.warning("Select at least one World Cup edition from the sidebar.")
    st.stop()

kpi_filtered = kpi[kpi["year"].isin(selected_years)].sort_values("year")
matches_filtered = matches[
    matches["year"].isin(selected_years)
    & matches["attendance"].between(attendance_range[0], attendance_range[1], inclusive="both")
].copy()

st.markdown(
    """
    <section class="hero">
        <div>
            <h1>FIFA World Cup Analytics</h1>
            <p>
                A polished data analyst dashboard covering tournament evolution, scoring trends,
                attendance dynamics, host impact, and a 2026 projection scenario.
            </p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-kicker">Executive overview</div>', unsafe_allow_html=True)
st.subheader("Tournament performance at a glance")

visual_cols = st.columns(3)
for column, visual in zip(visual_cols, VISUALS):
    with column:
        st.image(visual["url"], caption=visual["title"], use_container_width=True)

total_goals = matches_filtered["total_goals"].sum()
avg_goals = matches_filtered["total_goals"].mean()
avg_attendance = matches_filtered["attendance"].mean()
total_attendance = matches_filtered["attendance"].sum()

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Total goals", compact_number(total_goals), "Goals scored in selected matches")
with c2:
    metric_card("Goals / match", f"{avg_goals:.2f}" if not pd.isna(avg_goals) else "N/A", "Offensive intensity")
with c3:
    metric_card("Avg attendance", compact_number(avg_attendance), "Average crowd per match")
with c4:
    metric_card("Total attendance", compact_number(total_attendance), "Stadium audience volume")

st.divider()

trend_tab, matches_tab, projection_tab, data_tab = st.tabs(
    ["Trends", "Match Explorer", "Projection 2026", "Data Tables"]
)

with trend_tab:
    left, right = st.columns((1.15, 0.85))
    with left:
        st.markdown('<div class="section-kicker">Scoring trend</div>', unsafe_allow_html=True)
        st.line_chart(kpi_filtered.set_index("year")["goals_per_match"], height=360)
    with right:
        st.markdown('<div class="section-kicker">Tournament scale</div>', unsafe_allow_html=True)
        chart_data = kpi_filtered.set_index("year")[["matches", "teams"]]
        st.bar_chart(chart_data, height=360)

    st.markdown('<div class="section-kicker">Attendance</div>', unsafe_allow_html=True)
    attendance_data = kpi_filtered.set_index("year")[["avg_attendance", "total_attendance"]]
    st.line_chart(attendance_data, height=320)

with matches_tab:
    st.markdown('<div class="section-kicker">Deep dive</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns((0.7, 0.3))
    with col_a:
        search = st.text_input("Search team, city, stadium or stage", placeholder="France, Final, Doha...")
    with col_b:
        sort_by = st.selectbox("Sort by", ["year", "total_goals", "attendance"], index=0)

    explorer = matches_filtered.copy()
    if search:
        search_columns = ["stage", "stadium", "city", "home_team_name", "away_team_name"]
        mask = pd.Series(False, index=explorer.index)
        for column in search_columns:
            mask = mask | explorer[column].astype(str).str.contains(search, case=False, na=False)
        explorer = explorer[mask]

    explorer = explorer.sort_values(sort_by, ascending=False if sort_by != "year" else True)
    st.dataframe(
        explorer[
            [
                "year",
                "stage",
                "city",
                "stadium",
                "home_team_name",
                "home_team_goals",
                "away_team_goals",
                "away_team_name",
                "attendance",
                "total_goals",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

with projection_tab:
    st.markdown('<div class="section-kicker">Scenario planning</div>', unsafe_allow_html=True)
    st.subheader("2026 format projection")
    p1, p2, p3 = st.columns(3)
    p1.metric("Expected matches", int(projection.loc[0, "expected_matches"]))
    p2.metric("Expected teams", int(projection.loc[0, "expected_teams"]))
    p3.metric("Estimated total goals", f'{projection.loc[0, "Total_goals"]:.1f}')

    st.write(
        "The estimate uses recent World Cup scoring averages and applies them to the expanded 48-team format."
    )
    st.dataframe(projection, use_container_width=True, hide_index=True)

with data_tab:
    st.markdown('<div class="section-kicker">Source outputs</div>', unsafe_allow_html=True)
    st.subheader("Clean KPI dataset")
    st.dataframe(kpi_filtered, use_container_width=True, hide_index=True)
    st.subheader("Filtered match dataset")
    st.dataframe(matches_filtered, use_container_width=True, hide_index=True)

st.caption("Built with Python, Pandas, Streamlit, and Power BI.")
