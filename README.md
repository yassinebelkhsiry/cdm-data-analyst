# ⚽ FIFA World Cup Data Analyst Project (1930–2022)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📊 Power BI Dashboard

![Dashboard](assets/dashboard.png)

## 📈 Goals Evolution

![Goals](assets/goals_trend.png)

## 📌 KPI Cards

![KPIs](assets/kpi_cards.png)

---

## 🏆 Project Overview

End-to-end Data Analyst project based on FIFA World Cup historical data (1930–2022).

Professional workflow:

Data Cleaning → EDA → KPI Engineering → Business Insights → Power BI → 2026 Projection

This project transforms raw football datasets into actionable insights using Python and Power BI.

---

## 🎯 Objectives

- Analyze tournament evolution  
- Identify dominant countries  
- Study offensive trends  
- Measure attendance impact  
- Evaluate host advantage  
- Compare 2018 vs 2022  
- Project 2026 (48 teams)

---

## 📂 Dataset

Files:

- WorldCupMatches.csv  
- WorldCupPlayers.csv  
- GoalScorers.csv  

Source: Kaggle

---

## 🛠 Tech Stack

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook  
- Power BI  

---

## 📊 KPIs

- Goals per match  
- Total goals  
- Average attendance  
- Goals per team  
- Titles per country  

Dynamic computation:

```python
latest_year = cups["Year"].max()
cups[cups["Year"] == latest_year]
