import bibtexparser
import json
from serpapi import GoogleSearch
import urllib.parse

SerpAPIkey="d6df6cf2b22e2b86f319abb1a995cfbfb9e3e9eb21bc1f65dc0087eff134a350"
params = {
	"api_key": "d6df6cf2b22e2b86f319abb1a995cfbfb9e3e9eb21bc1f65dc0087eff134a350",
	"device": "desktop",
	"engine": "google_scholar",
	"q": "Subhrendu",
	"num": "1",
	"hl": "en"
}
#############################################################
with open('mypub.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
bibList=bib_database.entries
#############################################################
#############################################################
for item in bibList:
	title=item['title']
	authors=item['author'].split(" and ")
	authList=[a.split(", ")for a in authors]
	
	params['q']= title
	search = GoogleSearch(params)
	results = search.get_dict()
	results['organic_results'][0]['publication_info']['authors'][0]

#############################################################
	print(item['author'])
print(bib_database.entries)