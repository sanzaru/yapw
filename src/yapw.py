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

import functions
from functions import *


# Globals
#_VERSION
_PORTNO = 0
_MAXCLI = 0
_VERSION = "0.0.2"

# Check the operating system and set variable
#winpath = "C:\\"
#if( os.path(winpath) ):
  #_PLATFORM = "win"
#else:
  #_PLATFORM = "unix"

  
# read in the configuration
readConfig()
# init our socket
server=init()
srvSock = [server]
  
# wait for next client to connect
while 1:
	inputready,outputready,exceptready = select.select(srvSock,[],[])
	
	for s in inputready:
		
		if s == server:
			connection, address = s.accept()
			srvSock.append(connection)
			print "Connected: ",address
		else:
			data = s.recv(1024)
			if data:
				print "DATA!\n"
				print "Data == \n" + data
				if data == "^":
					print "!! CATCH !!\n"
					sys.exit()
				elif "GET /" in data:
					print "GET!\n"
					page = str(getReqPage(data))
					s.send(page)
					s.close()
					srvSock.remove(s)
					break
				else:
					s.send("Error: Unknown Command!\r\n")
					break
			else:
				print "Client ("+str(address)+" disconnected!"
				s.close()
				srvSock.remove(s)
				
s.close()
