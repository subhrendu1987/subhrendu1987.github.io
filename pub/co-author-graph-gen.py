import bibtexparser
import json
import urllib
import urllib.parse
#from chord import Chord
from itertools import combinations
import pandas as pd
import networkx as nx
import xmltodict
import os
import numpy as np
#import holoviews as hv
#from holoviews import opts, dim
#import holoviews.plotting.bokeh
DBLP_URL="https://dblp.org/pid/141/2034.xml"
BIB_FILE="common/20_bibilography/mypub.bib"
PI=np.pi
#############################################################
def createLegend(G):
    legendList={}
    reverseLegend={}
    for i,name in enumerate(list(G.nodes())):
    	legendList[name]=i+1
    	reverseLegend[i+1]=name
    return ((legendList,reverseLegend))
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
def bibListToNetx(bibList):
	coauthCount={}
	G=nx.multigraph.Graph()
	if(len(bibList)==0):
		bibList=fetchFromBib()
	for pub in bibList:
		title=pub['title']
		authors=pub['author'].split(" and ")  # Last Name First Format
		## Process Authors
		authors_formatted=[]
		for auth in authors:
			temp=auth.split(",")
			if(len(temp)==2):
				authors_formatted.append((temp[1]+" "+temp[0]).strip())
			else:
				print("3 Part Author name: Check entry: "+title)
		coauthors=list(combinations(authors_formatted, 2))
		#coauthors=list(combinations(authors, 2))
		for auth2 in coauthors:
			if G.has_edge(auth2[0],auth2[1]):
				G.add_edge(auth2[0],auth2[1],weight=G[auth2[0]][auth2[1]]['weight']+1)
			else:
				G.add_edge(auth2[0],auth2[1],weight=1)
	return(G)
#############################################################
def graphToHTML(G,chart_gen_code_body_file):
	#HTMLs=[]
	with open("weighted.coauthlist.tmp") as file:
		lines=file.readlines()
	LNs=[l.strip().split(",") for l in lines]
	
	with open(chart_gen_code_body_file, "w+") as myfile:
		for l in LNs:
		  	htmlSyntax="{ source: \""+str(legendList[l[0].strip()])+"\", target: \""+str(legendList[l[1].strip()])+"\", value: "+str(l[2].strip())+"}"
		  	#HTMLs.append(htmlSyntax)
		  	myfile.write(htmlSyntax+",\n")
		myfile.write("]); // Make stuff animate on load\n")
		myfile.write(" series.appear(500, 100);\n")
		myfile.write("}); // end\n")
		myfile.write("\n am5.ready()\n")
		myfile.write("</script>\n")

	return
#############################################################
def legendToHTML(reverseLegend,chart_gen_code_legend_file):
	#HTMLs=[]
	with open(chart_gen_code_legend_file, "w+") as myfile:
		myfile.write("<div id=\"chartdiv\"></div>\n")
		myfile.write("<h2>Legends</h2>\n")
		myfile.write("<ol>\n")
		for k in reverseLegend.keys():
			htmlSyntax="<li> "+str(reverseLegend[k])+"</li>"
			#HTMLs.append(htmlSyntax)
			myfile.write(htmlSyntax+"\n")
		myfile.write("</ol>")
	return
#############################################################
G=bibListToNetx([])
legendList,reverseLegend =createLegend(G)
nx.write_weighted_edgelist(G, "weighted.coauthlist.tmp", delimiter=",")
chart_gen_code_body_file="ChartData-2.html"
graphToHTML(G,chart_gen_code_body_file)

chart_gen_code_legend_file="ChartData-3.html"
legendToHTML(reverseLegend,chart_gen_code_legend_file)


os.system("cat ChartData-1.html ChartData-2.html ChartData-3.html> ChartData.html")

print("cat ChartData-1.html ChartData-2.html ChartData-3.html ChartData-4.html > ChartData.html")
print("Use https://www.amcharts.com/demos/chord-diagram/ to generate chord diagram.")
#############################################################