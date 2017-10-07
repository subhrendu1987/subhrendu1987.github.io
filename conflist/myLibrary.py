#!/usr/bin/python
import datetime,subprocess,sys,os,json
import time,hashlib
from random import randint
import random, re, commands
from time import sleep
from copy import copy
from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
############################################################################
folders="/home/pi/flipperRPi3/"
log_file=folders+"LOG/log.txt"
############################################################################
def hash_dict(d):
    return hashlib.sha1(json.dumps(d, sort_keys=True)).hexdigest()
############################################################################
def getTimeStamp():
	tstamp = str(datetime.datetime.now())
	return(tstamp)
############################################################################
def printToLog(filename,logtext):
	file_handler=open(filename,"a")
	tstamp = getTimeStamp()
	log_string="%s\t %s\n"%(tstamp,logtext)
	file_handler.write(log_string)
	file_handler.close()
	return
############################################################################
def add_to_log(log):
	file_handler=open(log_file,"a")
	tstamp = getTimeStamp()
	log_string="%s\t %s\n"%(tstamp,log)
	file_handler.write(log_string)
	file_handler.close()
	return log_string
############################################################################
def getDictTSV(filename):
	lines=[line.strip().split("\t") for line in open(filename, 'r')]
	variable={l[0]:l[1] for l in lines}
	return(variable)
############################################################################
def getDictFrom(filename):
	file_handler=open(filename,"r")
	variable=json.load(file_handler)
	file_handler.close()
	return(variable)
############################################################################
def putDictTo(filename,variable):
	file_handler=open(filename,"w")
	json.dump(variable, file_handler)
	file_handler.flush()
	file_handler.close()
	return
############################################################################
def ExactAcronym(ListOfRows,acronym,Title=None):
	indices=[i for i,R in enumerate(ListOfRows) if R["Acronym"]==acronym]
	match=[(i,SequenceMatcher(None, R["Title"], Title).ratio()) for i,R in enumerate(ListOfRows)]
	match=sorted(match, key=lambda x: x[1],reverse=True)
	matchPercentage=[i for i,R in enumerate(ListOfRows) if SequenceMatcher(None, R["Title"], Title).ratio() ==1.0]
	if len(indices)==1:
		return(indices[0])
	elif(len(matchPercentage)==1):
		return(matchPercentage[0])
	else:
		print "------------------------------------------------------------------------"
		print "Suggestions:"
		print "Acronym Match Index: [%s]"%(str(indices))
		print "Title Match Index: [%s]"%(str(match))  
		print "------------------------------------------------------------------------"
		return(None)
############################################################################
def GetConferenceRanking(acronym,Title=None):
	''' Parse Core'''
	URL="http://portal.core.edu.au/conf-ranks/?search=%s&by=all&source=all&sort=atitle&page=1"%(acronym)
	r  = requests.get(URL)
	data = r.text
	LeftPos=data.find("of",data.find("Showing results"))+len("of")
	RightPos=data.find("\n",LeftPos)
	choice=False
	try:
		Results=int(data[LeftPos:RightPos])
		if Results <>1:
			choice=True
		DataSoup = BeautifulSoup(data)
		table=DataSoup.find_all("table")
		SoupRows=BeautifulSoup(str(table[0]))
		rows=SoupRows.find_all("tr")
		SoupCols=BeautifulSoup(str(rows[0]))
		cols=SoupCols.find_all("th")
		items=[re.sub("\n","",c.get_text()).strip()  for c in cols]
		Names=SoupCols.findChildren("b")
		headers=[str(h.get_text()) for h in Names]
		ListOfRows=[]
		print "------------------------------------------------------------------------"
		for i,r in enumerate(rows[1:]):
			SoupCols=BeautifulSoup(str(r))
			cols=SoupCols.find_all("td")
			dt=[str(re.sub("\n","",c.get_text()).strip())  for c in cols]
			if (len(headers) <> len(dt)):
				print "ERROR: Table Parsing Problem. "+acronym
				return(None)
			TabDict={j:dt[i] for i,j in enumerate(headers)}
			ListOfRows=ListOfRows+[TabDict]
			matchPercentage=SequenceMatcher(None, TabDict["Title"], Title).ratio()
			print "%d:-->%s\t(%s)\t Match=%f"%(i,TabDict["Title"],TabDict["Acronym"],matchPercentage)
		if choice:
			if ExactAcronym(ListOfRows,acronym,Title) == None:
				print "------------------------------------------------------------------------"
				print "Enter your choice for search string (%s):"%(acronym)
				selected=input()
				print "------------------------------------------------------------------------"
			else:
				selected=ExactAcronym(ListOfRows,acronym,Title)
		else:
			selected=0
		TabDict=ListOfRows[selected]
	except Exception as e:
		print "ERROR: Conf. Name %s"%(acronym)
		return(None)
	return(TabDict)
############################################################################
def ParseTable(table_tag,head=None,Title=None,acronym=None):
	now=datetime.datetime.now()
	SoupRows=BeautifulSoup(table_tag)
	rows=SoupRows.find_all("tr")
	if(len(rows)==0):
		print "Error(%s:%s): No such conference"%(acronym,Title)
		return(None)
	if head==None:
		SoupCols=BeautifulSoup(str(rows[0]),"html.parser")
		headers=SoupCols.findChildren("td")
		H=[str(re.sub("\n","",c.get_text()).strip())  for c in headers]
	else:
		H=head
	noOfItems=len(rows)
	tab=[]
	for i,j in zip(xrange(1,noOfItems,2),xrange(2,noOfItems,2)):
		tabDict={}
		
		R=BeautifulSoup(str(rows[i])+str(rows[j]),"html.parser")
		dt=R.text.split("\n")
		try:
			dt.remove('')
		except ValueError:
			pass
		for x,h in enumerate(H):
			tabDict[h]=dt[x].encode('ascii','replace')
		try:
			''' Get year from acronym'''	
			if "(" in tabDict["Deadline"]:
				tabDict["Deadline"]=tabDict["Deadline"][:(tabDict["Deadline"].find("("))].strip()
			elif tabDict["Deadline"]=="TBD":
				tabDict["Deadline"]="TBD"
				tabDict["delta"]="TBD"
				break
			tabDict["Deadline"]=datetime.datetime.strptime(tabDict["Deadline"],"%b %d, %Y")
			tabDict["delta"]=(now - tabDict["Deadline"]).days
		except:
			print "ERROR:%s"%(tabDict["Acronym"])+" Date is not parsable [%s]"%(tabDict["Deadline"])
			return(None)
		tabDict["delta"]=(now - tabDict["Deadline"]).days
		tabDict["match"]=SequenceMatcher(None, tabDict["Title"], Title).ratio()
		tab=tab+[tabDict]
	return(tab)
############################################################################
def recentDates(SortedConfs,acronym):
	acro= acronym.lower()[acronym.find("+")+1:] if "+" in acronym else acronym.lower()
	if len(SortedConfs) <1:
		return None
	temp=SortedConfs[:]
	for dt in reversed(temp):
		d=dt["Acronym"].lower()
		pattern="%s [0-9]{4}"%(acro)
		if re.search(pattern,d, re.IGNORECASE):
			pass
		else:
			temp.remove(dt)
	if len(temp) <1:
		return(sorted(SortedConfs , key=lambda k: k['match'],reverse=True)[0]) #Use highest title matching value
	SortedConfs=temp
	now=datetime.datetime.now()
	if len(SortedConfs) > 1:
		if SortedConfs[1]["Deadline"].year > now.year:
			return(SortedConfs[1])
		else:
			return(SortedConfs[0])
	else:
		return(SortedConfs[0])
############################################################################
def GetConferenceCFPTable(acronym,Title=None):
	''' Parse wikiCFP'''
	URL="http://www.wikicfp.com/cfp/servlet/tool.search?q=%s&year=f"%(acronym)
	r  = requests.get(URL)
	data = r.text
	discardPos=data.find("Matched Call For Papers for")
	left=data[discardPos:]
	DataSoup = BeautifulSoup(left)
	table=str(DataSoup.find_all("table")[0])
	table_tag,head=table,["Acronym","Title","When","Where","Deadline"]
	CFPDict=ParseTable(table_tag,head,Title,acronym)
	return(CFPDict)
############################################################################
def GetConferenceCFP(acronym,Title=None):
	''' Parse wikiCFP'''
	URL="http://www.wikicfp.com/cfp/servlet/tool.search?q=%s&year=f"%(acronym)
	r  = requests.get(URL)
	data = r.text
	discardPos=data.find("Matched Call For Papers for")
	left=data[discardPos:]
	DataSoup = BeautifulSoup(left)
	table=str(DataSoup.find_all("table")[0])
	table_tag,head=table,["Acronym","Title","When","Where","Deadline"]
	CFPDict=ParseTable(table_tag,head,Title,acronym)
	if CFPDict==None:
		return(None)
	else:
		SortedConfs = sorted(CFPDict, key=lambda k: k['match'],reverse=True)
		SortedConfs= SortedConfs if len(SortedConfs) <5 else SortedConfs[:5]# Top 5 title matches
		SortedConfs = sorted(SortedConfs, key=lambda k: abs(k['delta']))
		data=recentDates(SortedConfs,acronym)
	return(data)
############################################################################
def PullRemoteFile(ip,filename):
		CMD="sshpass -p \"raspberry\" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@%s:%s /tmp/tmp.json" %(ip,filename)
		#CMD="sshpass -p \"raspberry\" scp pi@%s:%s /tmp/tmp.json"%(ip,filename)
		proc = subprocess.Popen(CMD,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		(out, err) = proc.communicate()
		if len(err) ==0:
			variable = getDictFrom("/tmp/tmp.json")
		else:
			print "SSH Error! "+err
			variable=None
		return(variable)
############################################################################
def PullRemoteFileWget(ip,filename,port=8080):
		tmp_file="/tmp/tmp.json"
		CMD="wget http://%s:%d/%s -O %s"%(ip,port,"LOG/"+os.path.basename(filename),tmp_file)
		proc = subprocess.Popen(CMD,shell=True, stdout=subprocess.PIPE)
		(out, err) = proc.communicate()
		#ret=os.system(CMD)
		if(ret==0):
			variable = getDictFrom(tmp_file)
			os.system("rm %s"%(tmp_file))
			return(variable)
		else:
			return(None)
############################################################################
