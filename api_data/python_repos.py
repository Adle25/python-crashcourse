import requests
import plotly.express as px


url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {
    'Accept': 'application/vnd.github.v3+json'
}

r = requests.get(url, headers=headers)

print(f'Status code: {r.status_code}')

data = r.json()

print(f'Complete results: {not data['incomplete_results']}')

repo_data = data['items']
repo_links, stars, hover_texts = [], [], []

for repository in repo_data:
    repo_name = repository['name']
    repo_url = repository['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)
    stars.append(repository['stargazers_count'])

    owner = repository['owner']['login']
    description = repository['description']
    hover_text = f'{owner}<br />{description}'
    hover_texts.append(hover_text)


title = 'Most-Starred Python Projects on Github'
labels = {
    'x': 'Repository',
    'y': 'Stars'
}

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()