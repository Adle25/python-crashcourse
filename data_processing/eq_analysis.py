from pathlib import Path
import json
import plotly.express as px


path = Path('data_processing/data/data.geojson')
contents = path.read_text(encoding='utf-8')
data = json.loads(contents)

eq_list = data['features']

mags = []
lons = []
lats = []
eq_titles = []

for eq in eq_list:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    eq_title = eq['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                    color=mags, color_continuous_scale='Viridis',
                    labels={'color': 'Magnitude'},
                    projection='natural earth',
                    hover_name=eq_titles
                )
fig.show()

