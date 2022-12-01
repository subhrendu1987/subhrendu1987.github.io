import bibtexparser
import json
from serpapi import GoogleSearch
import urllib.parse
from chord import Chord
from itertools import combinations
import pandas as pd
import networkx as nx

import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
#############################################################
'''
# Pandas is gonna be used to read the csv file stored on the web:


SerpAPIkey="d6df6cf2b22e2b86f319abb1a995cfbfb9e3e9eb21bc1f65dc0087eff134a350"
params = {
	"api_key": "d6df6cf2b22e2b86f319abb1a995cfbfb9e3e9eb21bc1f65dc0087eff134a350",
	"device": "desktop",
	"engine": "google_scholar",
	"q": "Subhrendu",
	"num": "1",
	"hl": "en",
	"output":"JSON"
}
'''
#############################################################
with open('mypub.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
bibList=bib_database.entries
#############################################################
coauthCount={}
G=nx.multigraph.Graph()
#############################################################
for pub in bibList:
	title=pub['title']
	authors=pub['author'].split(" and ")
	coauthors=list(combinations(authors, 2))
	for auth2 in coauthors:
		if G.has_edge(auth2[0],auth2[1]):
			G.add_edge(auth2[0],auth2[1],weight=G[auth2[0]][auth2[1]]['weight']+1)
		else:
			G.add_edge(auth2[0],auth2[1],weight=1)

df=nx.to_pandas_adjacency(G)
names = list(df.columns.values)
data = df.values.tolist()
'''
#add node labels
nodes = hv.Dataset(pd.DataFrame(data['nodes']), 'index')#create chord object
chord = hv.Chord((data, nodes)).select(value=(5, None))#customization of chart
chord.opts(
           opts.Chord(cmap='Category20', edge_cmap='Category20',                              edge_color=dim('source').str(), 
           labels='nodes', node_color=dim('index').str()))
'''
'''		
Chord(data, names).to_html("chord-diagram.html")
		if(auth in list(coauthCount.keys())):
			coauthCount[auth]=coauthCount[auth]+1
		else:
			coauthCount[auth]=1

# Names of the features.
names = ["Co-Author","Cumulative Citation"]
Chord(matrix, names, colors="d3.schemeDark2").to_html()
#############################################################