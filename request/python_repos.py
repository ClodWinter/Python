import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
dictResponse = r.json()

if r.status_code == 200:
	print(dictResponse["total_count"])
	items = dictResponse["items"]
	for item in items:
		print('\nName:', item['name']) 
		print('Owner:', item['owner']['login']) 
		print('Stars:', item['stargazers_count']) 
		print('Repository:', item['html_url']) 
		print('Description:', item['description'])