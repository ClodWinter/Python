import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
dictResponse = r.json()

if r.status_code == 200:
	names = []
	stars = []
	items = dictResponse["items"]
	for item in items:
		names.append(item['name'])
		stars.append(item['stargazers_count'])



	my_config = pygal.Config()
	my_config.x_label_rotation = 45
	my_config.show_legend = False
	my_config.title_font_size = 24
	my_config.label_font_size = 14
	my_config.major_label_font_size = 18
	my_config.truncate_label = 15
	my_config.show_y_guides = False
	my_config.width = 1000

	my_style = LS("#333366",base_style=LCS)
	chart= pygal.Bar(my_config,style = my_style)
	chart.title = 'GitHub'
	chart.x_labels = names

	chart.add('',stars)
	chart.render_to_file('python_repos.svg')