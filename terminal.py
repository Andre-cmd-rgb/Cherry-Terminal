import subprocess
import platform
import socket
import time
import os
##import wget
## Per Vigolini, wget non e riconosciuto

url = 'https://github.com/Andre-cmd-rgb/Cherry-Terminal/releases/download/0.4/terminal.py'
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Cherry Terminal [Version 0.3 beta]")
A = False
def madeit():
	print("No reward disponible for now, return on other versions with same credentials")
	print("!!! IT'S FORBIDDEN TO SHARE ANY INFO ON INTERNET")
while True:
	code = input(">>> ")
	if code == 'ping':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))
	if code == 'local':
		print("Your Local IPS Is: " + host_ip)
		print("Your Desktop Name Is: " + host_name)
	if code == 'date':
		print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
	if code == 'ls':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)
	if code == 'ls -a':
		file = input("Enter The Direct File Path To Read: ")
		dir_list2 = os.listdir(file)
		print("Files and directories in '", file, "':")
		print(dir_list2)
	if code == 'echo':
		echo = input("What Do You Want Me To Echo:")
	if code == 'help':
		print('aviable commands:')
		print('ping')
		print('local')
		print('date')
		print('ls')
		print('ls -a')
		print('echo')
		print('cd')
		print("mistery_login")
		print('exit')
	if code == 'exit':
		os.system(exit)
	if code == 'cd':
		chdir = input("Where do you want to cd:")
		os.chdir(chdir)
	if code == 'upgrade':
		filename = wget.download(url)
		os.remove("terminal.py")
		os.rename('terminal (1).py', 'terminal.py')
		os.system(exit)
	if code == "mistery_login":
		print("This is a built-in game, with the given information you need to find the user login and password.")
		print("First clue: it's a stupid person and doesn't know much about security.")
		print("His name is Gigio and surname Giangio.")
		print("His zoodiacal sign is Cancer and he's born the 21 in the 'Millenium bug year'")
		print("He never put spaces or signs in his texts.")
		A = True
		while A == True :
			usr = input("Username: ")
			if usr == "GigioGiangio":
				print("Good morning Gigio")
				psw = input("Password: ")
			else:
				A = False
				
			if psw == "21072000":
				print("Congrats, you made it!")
				madeit()
				A = False
			else:
				print("Nope")
				A = False
				


