#!/usr/bin/env python

import http.server
import socketserver
class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()


print (cl.blue+"""

	*--------------------------------------*
	|       programmed by : Abdessmad      |
	|               BlackTeam              |
	*--------------------------------------*
     ____  _            _    _____                    
    | __ )| | __ _  ___| | _|_   _|__  __ _ _ __ ___  
    |  _ \| |/ _` |/ __| |/ / | |/ _ \/ _` | '_ ` _ \ 
    | |_) | | (_| | (__|   <  | |  __/ (_| | | | | | |
    |____/|_|\__,_|\___|_|\_\ |_|\___|\__,_|_| |_| |_|
 
	             SimpleHTTPServer             
	            ----------------        
	            
"""+cl.end)

port = 4444

server = http.server.SimpleHTTPRequestHandler
request = socketserver.TCPServer(("",port),server)
print("server is up ....",port)
request.serve_forever()
