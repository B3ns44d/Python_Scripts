#!/usr/bin/env python
class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()
    
import crypt, sys
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

def cracker(passcrypt, dicfile):
	dicfile = open(dicfile, 'r')
	for word in dicfile:
		password = word.strip('\n')
		cryptword = crypt.crypt(password, passcrypt)
		if cryptword == passcrypt:
			print("\n[+]Password Found: "+word)
			return True

	print("[-]Not Found!")

try:
	filepass = sys.argv[1]
	dictfile = sys.argv[2]
except:
	print('#Usage:\n\tpython linuxcracker.py passfile.txt dictfile.txt')
	exit(0)

readpass = open(filepass, 'r')

for line in readpass:
	user = line.split(':')[0]
	cryptpass = line.split(':')[1].strip(' ')
	print("[*] Cracking | User: "+user)
	cracker(cryptpass, dictfile)

