import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle


filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)


dictPop = {}
for dict in pop_data:
	if dict['Year'] == '2010':
		countryname = dict['Country Name']
		population = int(float(dict['Value']))
		code = get_country_code(countryname)
		if code:
			dictPop[code] = population


dictPop1,dictPop2,dictPod3 = {},{},{}

for cc,pop in dictPop.items():
	if pop<10000000:
		dictPop1[cc] = pop
	elif pop<1000000000:
		dictPop2[cc] = pop
	else:
		dictPod3[cc] = pop


c_style = RotateStyle('#336699',base_style = LightColorizedStyle)
wm = pygal.maps.world.World(style = c_style)
wm.title = '世界人口地图'
wm.add('0-10k',dictPop1)
wm.add('10m-1bn',dictPop2)
wm.add('>1bn',dictPod3)
wm.render_to_file('world_population.svg')



