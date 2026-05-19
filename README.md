# CDM Data Analyst - Analyse de la Coupe du Monde FIFA

![Banniere Coupe du Monde](https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=1600&q=80)

## Presentation du projet

Ce projet est un travail d'analyse de donnees sur la Coupe du Monde FIFA, de 1930 a 2022.

L'objectif est simple : partir de fichiers de donnees bruts, les nettoyer, les analyser, puis les transformer en tableaux, indicateurs et graphiques faciles a comprendre.

En clair, ce projet montre comment un Data Analyst travaille sur un vrai sujet :

1. Recuperer des donnees.
2. Corriger les erreurs et rendre les colonnes propres.
3. Calculer des indicateurs importants.
4. Repondre a des questions metier.
5. Creer des visualisations.
6. Construire un dashboard interactif.
7. Proposer une projection pour la Coupe du Monde 2026.

## Idee generale

La Coupe du Monde est un bon sujet d'analyse car elle contient beaucoup d'informations interessantes :

- les matchs joues par edition ;
- les equipes presentes ;
- le nombre de buts marques ;
- l'affluence dans les stades ;
- l'evolution du format du tournoi ;
- les differences entre les anciennes editions et les editions modernes ;
- l'impact possible du passage a 48 equipes en 2026.

Le but n'est pas seulement de faire du code. Le but est surtout de raconter une histoire avec les donnees.

## Apercu visuel

| Ambiance du tournoi | Intensite des matchs | Analyse des donnees |
| --- | --- | --- |
| ![Stade de football](https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80) | ![Match de football](https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&w=600&q=80) | ![Dashboard data](https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80) |

## Ce que contient le projet

Le projet contient plusieurs parties :

- des fichiers CSV avec les donnees de base ;
- des fichiers CSV nettoyes et prets pour l'analyse ;
- des notebooks Jupyter pour expliquer les etapes ;
- du code Python organise dans le dossier `src` ;
- une application Streamlit dans `main.py` ;
- une structure claire pour ajouter plus tard un dashboard Power BI ou un rapport final si besoin.

## Structure du projet

```text
.
|-- data/
|   |-- raw/
|   |   |-- GoalScorers.csv
|   |   |-- WorldCupMatches.csv
|   |   |-- WorldCupPlayers.csv
|   |-- processed/
|       |-- kpi_worldcup.csv
|       |-- matches_clean.csv
|       |-- players_clean.csv
|       |-- projection_2026.csv
|       |-- scorers_clean.csv
|-- notebooks/
|   |-- 01_load_data.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_analysis.ipynb
|   |-- 05_projection_2026.ipynb
|   |-- 06_champions_business.ipynb
|   |-- 07_host_attendance.ipynb
|   |-- 08_modern_kpi_dashboard.ipynb
|   |-- 09_projection_limits.ipynb
|-- src/
|   |-- analysis.py
|   |-- cleaning.py
|   |-- config.py
|   |-- features.py
|   |-- load_data.py
|   |-- projection.py
|   |-- visualization.py
|-- main.py
|-- requirements.txt
|-- README.md
```

## Explication simple des dossiers

### `data/raw`

Ce dossier contient les donnees originales.

Ce sont les fichiers de depart. On evite de les modifier directement afin de garder une version propre de la source.

### `data/processed`

Ce dossier contient les donnees nettoyees.

Par exemple :

- les noms de colonnes sont standardises ;
- les doublons sont retires ;
- les types de donnees sont corriges ;
- de nouvelles colonnes utiles sont ajoutees, comme le nombre total de buts par match.

### `src`

Ce dossier contient le code Python organise par role.

Chaque fichier a une responsabilite :

- `load_data.py` charge les fichiers CSV ;
- `cleaning.py` nettoie les donnees ;
- `features.py` cree de nouvelles variables utiles ;
- `analysis.py` calcule les indicateurs ;
- `projection.py` estime les valeurs pour 2026 ;
- `visualization.py` cree des graphiques ;
- `config.py` centralise les chemins du projet.

### `notebooks`

Les notebooks servent a documenter le raisonnement.

Ils permettent de tester, visualiser et expliquer les etapes de l'analyse de maniere progressive.

### `main.py`

Ce fichier lance l'application Streamlit.

Streamlit sert a creer une application web simple et interactive avec Python. Dans ce projet, elle permet de filtrer les annees, voir les KPIs, explorer les matchs et afficher une projection pour 2026.

## Technologies utilisees

| Technologie | Utilisation dans le projet |
| --- | --- |
| Python | Langage principal du projet |
| Pandas | Nettoyage, transformation et analyse des donnees |
| NumPy | Calculs numeriques |
| Matplotlib | Creation de graphiques |
| Streamlit | Dashboard interactif en ligne |
| Jupyter Notebook | Exploration et documentation de l'analyse |
| Git / GitHub | Versioning et partage du projet |

## Indicateurs analyses

Le projet calcule plusieurs indicateurs importants :

- nombre total de matchs ;
- nombre total de buts ;
- moyenne de buts par match ;
- affluence moyenne ;
- affluence totale ;
- nombre d'equipes par edition ;
- comparaison entre editions ;
- projection du nombre de buts en 2026.

## Questions auxquelles le projet repond

Ce projet cherche a repondre a plusieurs questions :

- Est-ce que la Coupe du Monde devient plus offensive avec le temps ?
- Est-ce que le nombre d'equipes influence le nombre de buts ?
- Est-ce que les editions recentes sont differentes des anciennes ?
- Quelles editions ont attire le plus de spectateurs ?
- Que peut-on attendre de la Coupe du Monde 2026 avec 48 equipes ?

## Dashboard Streamlit

Le dashboard Streamlit contient :

- une banniere visuelle ;
- des cartes KPI professionnelles ;
- un filtre par edition de Coupe du Monde ;
- un filtre par affluence ;
- des graphiques sur l'evolution des buts ;
- des graphiques sur l'affluence ;
- un explorateur de matchs avec recherche ;
- une section dediee a la projection 2026 ;
- des tables de donnees propres.

## Comment lancer le projet

### 1. Installer les dependances

Dans le terminal, se placer dans le dossier du projet puis executer :

```bash
pip install -r requirements.txt
```

Cette commande installe les bibliotheques necessaires au projet.

### 2. Lancer le dashboard

Executer ensuite :

```bash
streamlit run main.py
```

Streamlit ouvre une page web locale dans le navigateur.

Si la page ne s'ouvre pas automatiquement, il faut copier l'adresse affichee dans le terminal, par exemple :

```text
http://localhost:8501
```

## Exemple de lecture du dashboard

Si on selectionne toutes les editions :

- le dashboard affiche le total des buts marques ;
- il calcule la moyenne de buts par match ;
- il montre l'affluence moyenne ;
- il permet de voir les tendances sur plusieurs decennies.

Si on selectionne seulement 2018 et 2022 :

- on peut comparer les editions recentes ;
- on peut voir si le nombre de buts augmente ou baisse ;
- on peut analyser l'affluence et le volume de matchs.

## Projection 2026

La Coupe du Monde 2026 aura un format plus grand avec 48 equipes.

Le projet propose une estimation simple basee sur les tendances recentes :

- estimation du nombre total de buts ;
- estimation de la moyenne de buts par match ;
- estimation du nombre de buts par equipe.

Cette projection n'est pas une prediction parfaite. C'est une simulation simple pour montrer comment utiliser les donnees historiques afin d'estimer un scenario futur.

## Ce que ce projet montre dans un portfolio

Ce projet montre plusieurs competences importantes pour un profil Data Analyst :

- comprendre un dataset ;
- nettoyer des donnees ;
- organiser un projet Python ;
- creer des KPIs ;
- analyser des tendances ;
- produire des graphiques ;
- construire un dashboard ;
- expliquer les resultats simplement ;
- publier un projet sur GitHub.

## Ameliorations possibles

Le projet peut encore etre ameliore avec :

- un modele de prediction plus avance ;
- des graphiques Plotly interactifs ;
- une analyse detaillee par pays ;
- une analyse des meilleurs buteurs ;
- une version Power BI complete ;
- des captures d'ecran locales du dashboard ;
- un deploiement en ligne avec Streamlit Community Cloud.

## Auteur

Projet realise par Yassine Belkhsiry.

GitHub : <https://github.com/yassinebelkhsiry>

Depot du projet : <https://github.com/yassinebelkhsiry/cdm-data-analyst>
