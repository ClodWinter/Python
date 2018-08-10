from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
	for code,name in COUNTRIES.items():
		if country_name == name:
			return code

	return None
