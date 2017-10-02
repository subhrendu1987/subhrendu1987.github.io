#!/usr/bin/python
import datetime,subprocess,sys,os,json
import time,hashlib
from random import randint
import random, re, commands
from time import sleep
from copy import copy
from bs4 import BeautifulSoup
import requests
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
def GetConferenceRanking(acronym):
	''' Parse Core'''
	URL="http://portal.core.edu.au/conf-ranks/?search=%s&by=all&source=all&sort=atitle&page=1"%(acronym)
	r  = requests.get(URL)
	data = r.text
	LeftPos=data.find("of",data.find("Showing results"))+len("of")
	RightPos=data.find("\n",LeftPos)
	try:
		Results=int(data[LeftPos:RightPos])
		if Results <>1:
			print  "ERROR: "+acronym+" Multiple Results"
		DataSoup = BeautifulSoup(data)
		table=DataSoup.find_all("table")
		SoupCols=BeautifulSoup(str(table[0]))
		cols=SoupCols.find_all("td")
		items=[re.sub("\n","",c.get_text()).strip()  for c in cols]
		headers=SoupCols.findChildren("b")
		Names=[h.get_text() for h in headers]
		if (len(Names) <> len(items)):
			print "ERROR: Table Parsing Problem. "+acronym
		TabDict={j:items[i] for i,j in enumerate(Names)}
	except:
		print "ERROR: Conf. Name %s"%(acronym)
		return(None)
	return(TabDict)
############################################################################
def GetConferenceCFP(acronym):
	''' Parse wikiCFP'''
	URL="http://www.wikicfp.com/cfp/servlet/tool.search?q=%s&year=f"%(acronym)
	r  = requests.get(URL)
	data = r.text
	discardPos=data.find("Matched Call For Papers for")
	left=data[discardPos:]
	DataSoup = BeautifulSoup(left)
	table=str(DataSoup.find_all("table")[0]) # need to handle blank results
	SoupRows=BeautifulSoup(table)
	rows=SoupRows.find_all("tr")
	SoupCols=BeautifulSoup(str(rows[0]))
	headers=SoupCols.findChildren("td")
	headers=SoupCols.findChildren("b")


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
