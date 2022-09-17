#The EnDa Calculator's Essentials file

#Import needed modules
from colorama import Fore
import os
import time
from pystyle import Colors, Colorate
import datetime

#Define a banner with personalitation
def banner(option):
    if str(option) == "1":
        print(Colorate.Horizontal(Colors.green_to_blue,"""

███████╗███╗   ██╗██████╗  █████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔██╗ ██║██║  ██║███████║    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╗██║██║  ██║██╔══██║    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████╗██║ ╚████║██████╔╝██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                                                          
        """,1))
    elif str(option) == "2":
        print(Colorate.Horizontal(Colors.green_to_blue,"""

▓█████  ███▄    █ ▓█████▄  ▄▄▄          ▄████▄   ▄▄▄       ██▓     ▄████▄   █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒████▄       ▒██▀ ▀█  ▒████▄    ▓██▒    ▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██  ▀█ ██▒░██   █▌▒██  ▀█▄     ▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██    ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▒▒██░   ▓██░░▒████▓  ▓█   ▓██▒   ▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░     ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░      ░   ░ ░  ░ ░  ░   ░   ▒      ░          ░   ▒     ░ ░   ░         ░░░ ░ ░   ░ ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
   ░  ░         ░    ░          ░  ░   ░ ░            ░  ░    ░  ░░ ░         ░         ░  ░     ░  ░            ░ ░     ░     
                   ░                   ░                          ░                                                            
                                        
        """,1))
    elif str(option) == "3":
        print(Colorate.Horizontal(Colors.green_to_blue,"""
  _____       ____           ____      _            _       _             
 | ____|_ __ |  _ \  __ _   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 |  _| | '_ \| | | |/ _` | | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| | | | |_| | (_| | | |__| (_| | | (__| |_| | | (_| | || (_) | |   
 |_____|_| |_|____/ \__,_|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                
        """,1))
    else:
        print(Fore.RED + "The selected option for banner is not avaible!")
        print(Fore.MAGENTA + "[TIP]" + Fore.WHITE + " >> " + Fore.RED + "Please check the code on banner options!" + Fore.WHITE)

#Define a space function
def space():
    print()

#Define a clear terminal function
def clearConsole():
    command = "clear"
    if os.name in ("dos",'nt'):
        command = "cls"
    os.system(command)

#Define a funciton which verifies if modules are installed
def verify():
    try:
        import os
        import colorama
        import time
        import math
        import pystyle
        import random
    except:
        print(Fore.RED + "Something went wrong about modules!")
        print(Fore.MAGENTA + "[TIP]" + Fore.WHITE + " >> " + Fore.RED + "Please install all needed modules from requirements file!")
        space()
        time.sleep(10)
        exit()
    else:
        print(Fore.GREEN + "All modules are already installed!" + Fore.WHITE)

#Define a list of options
def options():
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " >> " + Fore.YELLOW + "Add")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " >> " + Fore.YELLOW + "Subtract")
    print(Fore.MAGENTA + "[3]" + Fore.WHITE + " >> " + Fore.YELLOW + "Multiply")
    print(Fore.MAGENTA + "[4]" + Fore.WHITE + " >> " + Fore.YELLOW + "Divide")
    print(Fore.MAGENTA + "[5]" + Fore.WHITE + " >> " + Fore.YELLOW + "Power")
    print(Fore.MAGENTA + "[6]" + Fore.WHITE + " >> " + Fore.YELLOW + "Root")

e = datetime.datetime.now()
today = e.strftime("%d/%m/%Y | %I:%M %p")

#Define a function to save the history to a text file
def saveHistory(x):
    try:
        with open("history.txt","a") as file:
            file.write(today + " - " + x + "\n")
    except:
        print(Fore.RED + "[ERROR] >> Something went wrong in saving this calculation to file!")
        space()
        time.sleep(10)
        exit()

#Powered by WBTER, EnDa Team in 2022