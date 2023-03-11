import webbrowser
import requests
site = input("Podaj adres strony: ")
dateOne = input("Podaj pierwsza date: ")
dateTwo = input("Podaj druga date: ")
dateThree = input("Podaj trzecia date: ")

url ="http://archive.org/wayback/available?url="+site+"&timestamp="+str(dateOne)
response = requests.get(url)
d = response.json()
pageOne = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(pageOne)

url ="http://archive.org/wayback/available?url="+site+"&timestamp="+str(dateTwo)
response = requests.get(url)
d = response.json()
pageTwo = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(pageTwo)

url ="http://archive.org/wayback/available?url="+site+"&timestamp="+str(dateThree)
response = requests.get(url)
d = response.json()
pageThree = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(pageThree)