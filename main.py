import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="CDM Data Analyst", layout="wide")

DATA = Path("data/processed")

st.title("⚽ CDM DATA ANALYST – FIFA World Cup")

@st.cache_data
def load_data():
    matches = pd.read_csv(DATA / "matches_clean.csv")
    kpi = pd.read_csv(DATA / "kpi_worldcup.csv")
    proj = pd.read_csv(DATA / "projection_2026.csv")
    return matches, kpi, proj

matches, kpi, proj = load_data()

# ================= SIDEBAR =================
st.sidebar.title("Filters")

years = st.sidebar.multiselect(
    "Select World Cup Year",
    sorted(kpi["year"].unique()),
    default=sorted(kpi["year"].unique())
)

kpi_f = kpi[kpi["year"].isin(years)]
matches_f = matches[matches["year"].isin(years)]

# ================= KPIs =================

c1,c2,c3 = st.columns(3)

c1.metric("⚽ Total Goals", int(matches_f["total_goals"].sum()))
c2.metric("📊 Goals per Match", round(matches_f["total_goals"].mean(),2))
c3.metric("👥 Avg Attendance", int(matches_f["attendance"].mean()))

st.divider()

# ================= TABLES =================

st.subheader("📋 Match Dataset")
st.dataframe(matches_f, use_container_width=True)

st.subheader("📊 KPI Table")
st.dataframe(kpi_f, use_container_width=True)

# ================= CHARTS =================

st.subheader("Goals per Match Evolution")
st.line_chart(kpi_f.set_index("year")["goals_per_match"])

st.subheader("Total Goals by World Cup")
st.bar_chart(kpi_f.set_index("year")["total_goals"])

# ================= MODERN =================

st.divider()
st.subheader("2018 vs 2022")

modern = kpi[kpi["year"].isin([2018,2022])]
st.dataframe(modern)

# ================= PROJECTION =================

st.divider()
st.subheader("🔮 Projection 2026")

st.dataframe(proj)

p1,p2,p3 = st.columns(3)
p1.metric("Total Goals", round(proj["Total_goals"][0],1))
p2.metric("Goals per Match", round(proj["Goals_per_match"][0],2))
p3.metric("Goals per Team", round(proj["Goals_per_team"][0],2))

st.markdown("""
### About
Interactive dashboard for FIFA World Cup analysis.

Author: Yassine – M1 Data Science
""")
