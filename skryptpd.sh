import webbrowser
import requests
dateOne = 20230125
dateTwo = 20220125
dateThree = 20210125

url ="http://archive.org/wayback/available?url="+"twitter.com"+"&timestamp="+str(dateOne)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url ="http://archive.org/wayback/available?url="+"twitter.com"+"&timestamp="+str(dateTwo)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url ="http://archive.org/wayback/available?url="+"twitter.com"+"&timestamp="+str(dateThree)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)