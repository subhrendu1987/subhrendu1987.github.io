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
import numpy as np
import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
DBLP_URL="https://dblp.org/pid/141/2034.xml"
BIB_FILE="0Subho_Resume/mypub.bib"
PI=np.pi
#############################################################
def check_data(df):
    L,M=data_matrix.shape
    if L!=M:
        raise ValueError('Data array must have (n,n) shape')
    return L
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
def get_ideogram_ends(ideogram_len, gap):
    ideo_ends=[]
    left=0
    for k in range(len(ideogram_len)):
        right=left+ideogram_len[k]
        ideo_ends.append([left, right])   
        left=right+gap
    return ideo_ends 
#############################################################
def moduloAB(x, a, b): #maps a real number onto the unit circle identified with 
                       #the interval [a,b), b-a=2*PI
        if a>=b:
            raise ValueError('Incorrect interval ends')
        y=(x-a)%(b-a)
        return y+b if y<0 else y+a
#############################################################
def test_2PI(x):
    return 0<= x <2*PI
#############################################################
def drawChordDiagram(df,outFile="chordDiagram.html"):
	check_data(df)
	df.drop('Chattopadhyay, Subhrendu', axis=0,inplace=True)
	df.drop('Chattopadhyay, Subhrendu', axis=1,inplace=True)
	names = list(df.columns.values)
	data = df.values.tolist()
	df.to_csv('out.csv')  
	matrix=df.to_numpy()

	row_sum=[np.sum(matrix[k,:]) for k in range(len(matrix))]
	#set the gap between two consecutive ideograms
	gap=2*PI*0.005
	ideogram_length=2*PI*np.asarray(row_sum)/sum(row_sum)-gap*np.ones(df.shape[0])
	ideo_ends=get_ideogram_ends(ideogram_length, gap)
	ideo_ends

	return
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

#############################################################
import pandas as pd
from bokeh.plotting import output_file, Chord
from bokeh.io import show
from bokeh.sampledata.les_mis import data




nodes = data['nodes']
links = data['links']

nodes_df = pd.DataFrame(nodes)
links_df = pd.DataFrame(links)

source_data = links_df.merge(nodes_df, how='left', left_on='source', right_index=True)
source_data = source_data.merge(nodes_df, how='left', left_on='target', right_index=True)
source_data = source_data[source_data["value"] > 5]

chord_from_df = Chord(source_data, source="name_x", target="name_y", value="value")
output_file('chord_from_df.html', mode="inline")
show(chord_from_df)
