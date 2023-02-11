import bibtexparser
import json
import urllib
import urllib.parse
#from chord import Chord
from itertools import combinations
#import pandas as pd
import networkx as nx
#import xmltodict
import os
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np
#import holoviews as hv
#from holoviews import opts, dim
#import holoviews.plotting.bokeh
DBLP_URL="https://dblp.org/pid/141/2034.xml"
BIB_FILE="common/20_bibilography/mypub.bib"
KEY_FILE="keywords"
#PI=np.pi
cmap = matplotlib.colors.ListedColormap(["#1A2C42","#BE2F29","#ECAF44"], name='from_list', N=None)
#cmap = matplotlib.colors.ListedColormap([rgba(26, 44, 66, 1),rgba(190, 47, 41, 1),rgba(236, 175, 68, 1),rgba(12, 17, 21, 1)], name='from_list', N=None)
#cmap = matplotlib.colors.ListedColormap([#1A2C42,#BE2F29,#ECAF44,#0C1115], name='from_list', N=None)
#############################################################
def fetchFromDBLP():
    file = urllib.request.urlopen(DBLP_URL)
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    pubList=data['dblpperson']['r']
    return (pubList)
#############################################################
def fetchKeywords():
	keywords=[]
	with open(KEY_FILE) as file:
	    lines=file.readlines()
	for line in lines:
		words=line.strip().split(";")
		words=[w.strip().replace(" ", "_") for w in words]
		keywords=keywords+ words
	return(keywords)
#############################################################
def fetchFromBib():
	with open(BIB_FILE) as bibtex_file:
	    bib_database = bibtexparser.load(bibtex_file)
	bibList=bib_database.entries
	return(bibList)
#############################################################
def bibListToAuthList(bibList):
	authList={}
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
		authList[title]=authors_formatted
	return(authList)
#############################################################
def bibListToNetx(bibList):
	coauthCount={}
	G=nx.multigraph.Graph()
	authList=bibListToAuthList([])
	for entry in authList:
		title=entry
		authors=authList[title]
		coauthors=list(combinations(authors, 2))
		for auth2 in coauthors:
			if G.has_edge(auth2[0],auth2[1]):
				G.add_edge(auth2[0],auth2[1],weight=G[auth2[0]][auth2[1]]['weight']+1)
			else:
				G.add_edge(auth2[0],auth2[1],weight=1)
	G.remove_node('Subhrendu Chattopadhyay')  # Remove own entry
	return(G)
#############################################################
def bibListToFreq(bibList):
	freqList={}
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
		for auth in authors_formatted:
			if(auth in freqList):
				freqList[auth]=freqList[auth]+1
			else:
				freqList[auth]=1
	del freqList['Subhrendu Chattopadhyay']  # Remove own entry
	return(freqList)
#############################################################
def createLegend(G):
    sortedNodeList=sorted(G.degree, key=lambda x: x[1], reverse=True)
    legendList={}
    reverseLegend={}
    for i,item in enumerate(sortedNodeList):
    	name=item[0]
    	legendList[name]=i+1
    	reverseLegend[i+1]=name
    return ((legendList,reverseLegend))
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
		
		myfile.write("<div style=\"width: 100%;\">\n")
		myfile.write("<div style=\"width: 70%; float: left;\" id=\"chartdiv\"></div>\n")
		myfile.write("<div style=\"width: 30%; float: left;\" id=\"chartlegend\">\n<h2>Legends</h2>\n")
		myfile.write("<ol>\n")
		for k in reverseLegend.keys():
			htmlSyntax="<li> "+str(reverseLegend[k])+"</li>"
			#HTMLs.append(htmlSyntax)
			myfile.write(htmlSyntax+"\n")
		myfile.write("</ol>\n</div>\n</div>\n")
		myfile.write("<h6>Used https://www.amcharts.com/demos/chord-diagram/ to generate chord diagram.</h6>")
	return
#############################################################
def createWordCloud(freq,file,maskFile=None):
	if(maskFile):
		mask_arr = np.array(Image.open(maskFile))
	else:
		mask_arr=None
	#wordcloud = WordCloud(mode="RGBA", background_color=None, colormap='tab10', mask=mask_arr)
	wordcloud = WordCloud(mode="RGBA", background_color=None, colormap=cmap, mask=mask_arr,collocations=False,width=800,height=400)
	wordcloud.generate_from_frequencies(frequencies=freq)
	plt.tight_layout(pad=0)
	plt.figure(figsize=(20,10))
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(file)
#############################################################
def createWordCloudKeyword(keyList,file,maskFile=None):
	if(maskFile):
		mask_arr = np.array(Image.open(maskFile))
	else:
		mask_arr=None
	#wordcloud = WordCloud(mode="RGBA", background_color=None, colormap='tab10', mask=mask_arr)
	wordcloud = WordCloud(mode="RGBA", background_color=None, colormap=cmap, mask=mask_arr,collocations=False,width=800,height=400)
	wordcloud.generate(" ".join(keyList))
	plt.tight_layout(pad=0)
	plt.figure(figsize=(20,10))
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(file)
#############################################################
G=bibListToNetx([])
authList=bibListToAuthList([])
legendList,reverseLegend =createLegend(G)
nx.write_weighted_edgelist(G, "weighted.coauthlist.tmp", delimiter=",")
chart_gen_code_body_file="Charts/ChartData-2.html"
graphToHTML(G,chart_gen_code_body_file)

chart_gen_code_legend_file="Charts/ChartData-3.html"
legendToHTML(reverseLegend,chart_gen_code_legend_file)
os.system("cat Charts/ChartData-1.html Charts/ChartData-2.html Charts/ChartData-3.html> Charts/ChartData.html")

freqList=bibListToFreq([])
createWordCloud(freqList,"Charts/authorWordCloud.png",maskFile="../imgs/clipartclouds.png")

keywords=fetchKeywords()
createWordCloudKeyword(keywords,"Charts/keywordWordCloud.png",maskFile="../imgs/clipartclouds.png")
#############################################################