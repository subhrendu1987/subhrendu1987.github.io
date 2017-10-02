#!/usr/bin/python
'''
Crawler for Conference ranking
'''
import datetime,subprocess,sys,os,json
import time,hashlib
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import random, re, commands
from time import sleep
from copy import copy
from datetime import datetime
from myLibrary import *
############################################################################
def GetHTMLTemplate(filename):
	data = [line.strip() for line in open(filename, 'r')]
	return(data)
############################################################################
def TruncateDict(D,items=None):
	if None:
		return(D)
	KEYS=D.keys()[0:items]
	ret={k:D[k] for k in KEYS}
	return(ret)
############################################################################
def generateHTML(message):
	m="\n".join(message)
	f = open('Conflist_Autognerated.html','w')
	f.write(m)
	f.close()
############################################################################
ConfList=getDictFrom("ConferenceRanking_All.json")
temp=TruncateDict(ConfList,5)
#Confs= [GetConferenceRanking(acronym) for acronym in ConfList]
#putDictTo("AllCOREdata.json",Confs)
Confs= [GetConferenceRanking(acronym) for acronym in temp]#Parse Core WebPage
####################################
SortedConfs = sorted(Confs, key=lambda k: k['Rank']) 
body1=GetHTMLTemplate("TemplateTop.html")
body3=GetHTMLTemplate("TemplateBottom.html")
body2=[]
Ranks=set([item['Rank'] for item in SortedConfs])
####################################
NAVBAR=[]
for r in Ranks:
	NAVBAR=NAVBAR+["<td class=\"Change Cicon\" style=\"width:75px\">",
		"<a id=\"NavBarLink\" class=\"NavLink\" href=\"#%s\">%s</a>"%(r.encode('ascii'), r.encode('ascii')),
		"</td>"]
body2=body2+["<table><tr align=\"center\">"]+NAVBAR+["</tr></table>"]	
body2=body2+["<!------------------------------------------------------------------------------------->"]
####################################
ConfTable=["<tr><th>Rank</th><th>Acronym</th><th>Title</th></tr>"]
for c in SortedConfs:
	ConfTable=ConfTable+["<tr>",
	"<td>%s</td>"%(c["Rank"].encode("ascii")),
	"<td><button class=\"gsearch\" onClick=\"googleSearch()\">%s</button></td>"%(c["Acronym"].encode("ascii")),
	"<td>%s</td></tr>"%(c["Title"].encode("ascii"))]
body2=body2+["<table border=\"1\"  width=\"70\%\">"]+ConfTable+["</table>"]
####################################
''' SAMPLE
<table border="1"  width="70%">
<tr><td><button class="gsearch" onClick="googleSearch()">	USITS	</button></td><td>	USENIX Conf on Internet Tech and Sys	</td></tr>
</table>
</center>
'''

body2=body2+["<h6>Last Updated:%s</h6>"%(getTimeStamp())]
message=body1+body2+body3
generateHTML(message)
