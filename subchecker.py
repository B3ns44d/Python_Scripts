#!/usr/bin/env python

yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"

print(blue+bold+"""
    *--------------------------------------*
	|       programmed by : Abdessmad      |
	|               BlackTeam              |
	*--------------------------------------*
     ____  _            _    _____                    
    | __ )| | __ _  ___| | _|_   _|__  __ _ _ __ ___  
    |  _ \| |/ _` |/ __| |/ / | |/ _ \/ _` | '_ ` _ \ 
    | |_) | | (_| | (__|   <  | |  __/ (_| | | | | | |
    |____/|_|\__,_|\___|_|\_\ |_|\___|\__,_|_| |_| |_|
                 
                   Coded by: Abdessmad                                  
                   ------------------

"""+end)


from concurrent.futures import ThreadPoolExecutor as executor # sudo pip install futures
import sys, requests, argparse


def printer(url):
	sys.stdout.write(url+"                                                                                             \r")
	sys.stdout.flush()
	return True



def check(out, url):
	printer("Testing: " + url)
	url = 'http://' + url
	try:
		req = requests.head(url, timeout=10)
		scode = str(req.status_code)
		if scode.startswith("2"):
			print(green + "[+] "+scode+" | Found: " + end + "[ " + url + " ]")
		elif scode.startswith("3"):
			link = req.headers['Location']
			print(yellow + "[*] "+scode+" | Redirection: " + end + "[ " + url + " ]" + yellow + " -> " + end + "[ " + link + " ]")
		elif st.startswith("4"):
			print(blue+"[!] "+scode+" | Check: " + end + "[ " + url + " ]")

		if out != 'None':
			with open(out, 'a') as f:
				f.write(url+"\n")
				f.close()

		return True

	except Exception:
		return False




def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-w", "--wordlist", help="Domains List File", type=str, required=True)
	parser.add_argument("-t", "--thread", help="Theads Number - (Default: 10)", type=int)
	parser.add_argument("-o", "--output", help="Save Results In a File", type=str) #action='store_true'

	args = parser.parse_args()

	wlist = str(args.wordlist)
	threads = str(args.thread)
	out = str(args.output)

	if threads == 'None':
		threads = 10
	else:
		threads = threads

	lines = len(open(wlist).readlines())
	print(blue +"["+red+"+"+blue+"] File: " + end + wlist)
	print(blue +"["+red+"+"+blue+"] Length: " + end + str(lines))
	print(blue +"["+red+"+"+blue+"] Threads: " + end + str(threads))
	print(blue +"["+red+"+"+blue+"] Output: " + end + str(out))
	print(red+bold+"\n[+] Results:\n"+end)

	urls = open(wlist, 'r')
	
	with executor(max_workers=int(threads)) as exe:
		[exe.submit(check, out, url.strip('\n')) for url in urls]




if __name__=='__main__':
	main()

