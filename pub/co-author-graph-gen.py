import bibtexparser
import json
import urllib
import urllib.parse
from chord import Chord
from itertools import combinations
import pandas as pd
import networkx as nx
import xmltodict
import os
import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
DBLP_URL="https://dblp.org/pid/141/2034.xml"
BIB_FILE="0Subho_Resume/mypub.bib"
#############################################################
def fetchFromDBLP():
    file = urllib.request.urlopen(DBLP_URL)
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    pubList=data['dblpperson']['r']
    return (pubList)
#############################################################
def fetchFromBib():
	with open(BIB_FILE) as bibtex_file:
	    bib_database = bibtexparser.load(bibtex_file)
	bibList=bib_database.entries
	return(bibList)
#############################################################
def bibListToNetx(bibList)
	coauthCount={}
	G=nx.multigraph.Graph()
	bibList=fetchFromBib()
	for pub in bibList:
		title=pub['title']
		authors=pub['author'].split(" and ")
		coauthors=list(combinations(authors, 2))
		for auth2 in coauthors:
			if G.has_edge(auth2[0],auth2[1]):
				G.add_edge(auth2[0],auth2[1],weight=G[auth2[0]][auth2[1]]['weight']+1)
			else:
				G.add_edge(auth2[0],auth2[1],weight=1)
	return(G)
#############################################################
G=bibListToNetx(bibList)
df=nx.to_pandas_adjacency(G)
names = list(df.columns.values)
data = df.values.tolist()
df.to_csv('out.csv')  


'''
pos=nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
'''
#############################################################
import plotly.plotly as py

'''
#add node labels
nodes = hv.Dataset(pd.DataFrame(data['nodes']), 'index')#create chord object
chord = hv.Chord((data, nodes)).select(value=(5, None))#customization of chart
chord.opts(
           opts.Chord(cmap='Category20', edge_cmap='Category20',                              edge_color=dim('source').str(), 
           labels='nodes', node_color=dim('index').str()))
'''
'''		
		if(auth in list(coauthCount.keys())):
			coauthCount[auth]=coauthCount[auth]+1
		else:
			coauthCount[auth]=1

# Names of the features.
names = ["Co-Author","Cumulative Citation"]
Chord(matrix, names, colors="d3.schemeDark2").to_html()
#############################################################