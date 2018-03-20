import requests
import json
from bs4 import BeautifulSoup
def main():
	www = 'https://gimmeproxy.com/api/getProxy'
	r = requests.get(www)
	data = json.loads(r.content)
	data = data['ip'].encode('utf-8')
	data = 'http://' + str(data)

	return data

if __name__ == '__main__':
	main()	