#!/usr/bin/python
'''
Crawler for Conference ranking and call for papers
'''
import datetime,subprocess,sys,os,json,pickle
import time,hashlib
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
ConfList=getDictTSV("ConferenceRanking_All.tsv")
putDictTo("ConferenceRanking_All.json",ConfList)
#ConfList=getDictFrom("ConferenceRanking_All.json")
Confs=[]
TierPriority={"A*":1,"A+":1,"A":2,"B":3,"C":4,"Australasian":5}
colors={100:"#ffffff",5:"#fdd0a2",4:"#fdae6b",3:"#fd8d3c",2:"#f16913",1:"#d94801"}
####################################
''' Use this part for Full list parsing
failed=[]
for acronym in ConfList:
	data=GetConferenceRanking(acronym,ConfList[acronym])
	if data <> None:
		Confs=Confs+[data]
	else:
		failed=failed+[acronym]
for c in Confs:
	if c["Rank"] in TierPriority.keys():
		c.update( {"Tier":TierPriority[c["Rank"]]})
	else:
		c.update( {"Tier":100}) # Very low priority
putDictTo("AllCOREdata.json",Confs)
####################################
Confs=getDictFrom("AllCOREdata.json")
'''
####################################
''' Use this part for Partial list parsing
temp=TruncateDict(ConfList,5)
Confs= [GetConferenceRanking(acronym) for acronym in temp]#Parse Core WebPage
'''
Confs=getDictFrom("AllCOREdata.json")
failed=[]
CFP_data={}
for i,c in enumerate(Confs):
	acronym,Title=c["Acronym"],c["Title"]
	print "<!------------------------------------------------------------------------------------->"
	print i,acronym,Title
	try:
		if acronym in CFP_data.keys():
			print "LOG:(%d. %s) Already exists"%(i,acronym)
			if CFP_data[acronym] == None:
				CFP_data[acronym]=GetConferenceCFP(acronym,Title)
				failed=failed+[(acronym,Title,"No CFP")]
				print "LOG:(%s) Retrying"%(i,acronym)
		else:
			CFP_data[acronym]=GetConferenceCFP(acronym,Title)
	except:
		raise
		failed=failed+[(acronym,Title,"ERROR")]
	notFound=[k for k in CFP_data.keys() if CFP_data[k] == None]
pickle.dump( CFP_data, open( "AllWIKICFPdata.pkl", "wb" ) )
####################################
'''
acronym="PERFORMANCE"
Data=GetConferenceCFPTable(acronym)
[d["Acronym"],d["Title"] for d in Data]
'''
####################################
SortedConfs = sorted(Confs, key=lambda k: k['Tier'])
body1=GetHTMLTemplate("TemplateTop.html")
body3=GetHTMLTemplate("TemplateBottom.html")
body2=[]
#Ranks=set([item['Rank'] for item in SortedConfs])
body2=body2+["<!------------------------------------------------------------------------------------->"]
####################################
now=datetime.datetime.now()
ConfTable=["<tr><th>Rank</th><th>Acronym</th><th>Title</th><th>CFP Name</th><th>Deadline</th><th>Days Left</th></tr>"]
for c in SortedConfs:
	if CFP_data[c["Acronym"]] <> None :
		deadline=CFP_data[c["Acronym"]]["Deadline"]
		delta=CFP_data[c["Acronym"]]["delta"]
		cfp_name=CFP_data[c["Acronym"]]["Acronym"]
		if deadline<> "TBD":
			deadline= deadline.strftime("%d-%m-%Y")
			days_left=str(abs(delta)) if CFP_data[c["Acronym"]]["Deadline"] > now else " Over"
		else:
			days_left,deadline="TBD","TBD"
	else:
		deadline,days_left,cfp_name="NA","NA","Not Found"
	cellcolor=colors[c["Tier"]]
	ConfTable=ConfTable+["<tr bgcolor=\"%s\">"%(cellcolor),
	"<td>%s</td>"%(c["Rank"].encode("ascii")),#Rank
	"<td><button class=\"gsearch\" onClick=\"googleSearch(this);\">%s</button></td>"%(c["Acronym"].encode("ascii")),#Acronym
	"<td>%s</td>"%(c["Title"].encode("ascii")),#Title
	"<td>%s</td>"%(cfp_name),#CFP Name
	"<td>%s</td>"%deadline,#Deadline
	"<td>%s</td>"%days_left,#Days Left
	"</tr>"]
body2=body2+["<table border=\"1\"  width=\"70\%\">"]+ConfTable+["</table>"]
####################################
body2=body2+["<h6>Last Updated:%s</h6>"%(getTimeStamp())]
message=body1+body2+body3
generateHTML(message)
