from colorama import Back, Fore, init

init()

def fore_red(msg):
	return Fore.RED + msg + Fore.RESET

def fore_green(msg):
	return Fore.GREEN + msg + Fore.RESET

def fore_yellow(msg):
	return Fore.YELLOW + msg + Fore.RESET

def fore_blue(msg):
	return Fore.BLUE + msg + Fore.RESET

def back_red(msg):
	return Back.RED + msg + Back.RESET

def back_green(msg):
	return Back.GREEN + msg + Back.RESET

def back_yellow(msg):
	return Back.YELLOW + msg + Back.RESET

def back_blue(msg):
	return Back.BLUE + msg + Back.RESET
