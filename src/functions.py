#--------------------------------------------------------------------------------------------------
# YAPW - Yet another python webserver
#
# Author: Martin Albrecht <martin.albrecht@javacoffee.de>
# Homepage: http://code.javacoffee.de
#
# Copyright (C) 2008 Martin Albrecht <martin.albrecht@javacoffee.de>
#
# This program is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation; either version 3 of the License, or 
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program; if not, see http://www.gnu.org/licenses/.
#--------------------------------------------------------------------------------------------------

import _socket
from _socket import *
import select

import sys
import time
import datetime
import re
import os

# initialize socket
def init():
	global _PORTNO
	global _MAXCLI

	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.bind(("", int(_PORTNO)))        
		s.listen(int(_MAXCLI))
		print "Socket created!\nListening on port "+str(_PORTNO)+" and can take "+str(_MAXCLI)+" connections!\n"
		return s                        
	except error, (value, message):
		print "Error: Cannot create and bind the socket!\nMessage: "+message+"\n"
		sys.exit(1)
		

# read page in www/ directory
def loadPage(page):        
	if page == "":
		page = "index.html"
	try:
		print "Loading page "+page+"..."
		f = open("www/"+page, "r")
		buffer = f.read()                              
		f.close()
		print "Page loaded!"
		return buffer
	except IOError,parameter:
		f = open("www/404.htm", "r")
		buffer = f.read()                              
		f.close()
		return buffer
  

# Write the access log  
def writeAccLog(address, data):
  now = time.strftime('%d.%m.%y - %H:%M:%S')
  date = time.strftime('%d%m%y')
  try:
    filename = "logs\\access"+date+".log"
    f=open(filename, "a")
    a=str(address)
    f.write(now+" : "+a+"\n"+data+"\n")
    f.close()
  except IOError,parameter:
    print "Error: Could not open access.log file!"
    return
    
  return
  
  
# Parse the HTTP request for requested page
# to load
def getReqPage(request):
  page = re.search("GET /(.*) ", request)
  p = loadPage(page.group(1))
  return p
  
  
#
# Read in the config file
def readConfig():
	global _PORTNO
	global _MAXCLI

	f = open("yapw.cnf", "r")
	conf = f.read()
	f.close()

	port = re.search("_PORTNO (.*)", conf)
	if port == "" or not port:
		_PORTNO = 80
		print "Defaulting port to "+str(_PORTNO)+"!\n"
	else:
		_PORTNO = port.group(1)
		print "Port number set to: "+str(_PORTNO)+"!\n"
		
	maxcli = re.search("_MAXCLI (.*)", conf)
	if maxcli == "" or not maxcli:
		_MAXCLI = 200
	else:
		_MAXCLI = maxcli.group(1)
