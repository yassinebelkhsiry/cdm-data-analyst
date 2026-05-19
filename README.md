# CDM Data Analyst - FIFA World Cup Analytics

Professional data analysis project about the FIFA World Cup from 1930 to 2022, with a Streamlit dashboard, cleaned datasets, notebooks, a Power BI file, and a simple 2026 projection.

## Overview

This project follows a practical data analyst workflow:

1. Load raw World Cup datasets
2. Clean and standardize the data
3. Build tournament KPIs
4. Explore business questions
5. Visualize trends in Python and Power BI
6. Estimate a 2026 expanded-format scenario

## Key Questions

- How did World Cup scoring evolve over time?
- Did the tournament format increase the number of goals?
- Which editions had the strongest attendance?
- How do recent tournaments compare?
- What can recent trends suggest for the 2026 World Cup?

## Dashboard Preview

The Streamlit app includes:

- Executive KPI cards
- Year and attendance filters
- Scoring, attendance, team, and match trends
- Match explorer with search
- 2026 projection summary
- Clean dataset tables

## Project Structure

```text
.
├── dashboard/
│   └── WorldCup.pbix
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── reports/
│   └── figures/
├── src/
│   ├── analysis.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── load_data.py
│   ├── projection.py
│   └── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook
- Power BI

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run main.py
```

## Outputs

- `data/processed/matches_clean.csv`
- `data/processed/kpi_worldcup.csv`
- `data/processed/projection_2026.csv`
- `dashboard/WorldCup.pbix`
- `reports/figures/final_report.pdf`

## Author

Yassine Belkhsiry  
GitHub: <https://github.com/yassinebelkhsiry>
