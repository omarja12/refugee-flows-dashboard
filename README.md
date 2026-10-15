# Refugee Flows Dashboard

An interactive [Dash](https://dash.plotly.com/) dashboard on refugee movements from 2001 to 2019, built with Plotly and Dash Bootstrap Components on UNHCR statistics (about 68,000 origin-to-asylum country flows).

## What it shows

| Tab | Views |
|---|---|
| Refugees, from where and to where? | a world choropleth (log scale) and the top countries of origin or asylum for a chosen year |
| What routes do refugees take? | a Sankey diagram of the largest flows between continents or regions |
| Who are the refugees? | a sunburst of the population by gender or age group, and its trend over a chosen range of years, per country or in total |

## Run it

```bash
pip install -r requirements.txt
python app.py                 # http://127.0.0.1:8050
gunicorn app:server           # production server, as in the Procfile
```

`python check.py` loads the app, requests the page and layout, and calls every callback for every year, segment and grouping the controls offer. The GitHub Actions workflow runs it on every push and starts the app under gunicorn.

## Layout

```
app.py            layout, callbacks and figures
assets/style.css  styling, loaded automatically by Dash
data/             the six prepared tables the app reads
check.py          smoke check
Procfile          gunicorn entry point for Heroku-style hosts
```

## Notes

- In the "Total" view the sunburst counts stateless and unknown-origin people, while the gender and age trend lines do not, so their totals differ slightly.
- The data tables are already aggregated; the preparation step is not included.

## Data

[UNHCR Refugee Data Finder](https://www.unhcr.org/refugee-statistics/). This project is independent and not affiliated with or endorsed by UNHCR.
