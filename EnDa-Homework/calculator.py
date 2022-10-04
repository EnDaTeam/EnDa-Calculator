#The EnDa Calculator's source code

#Import modules
from Tools.essentials import *
from colorama import Fore
import math
from random import randint

#Import custom modules
from Tools.mathfunctions import *


#Constants
pi = math.pi
euler = math.e

value = randint(1,3)

#Create a start up
clearConsole()
space()
banner(value)
space()
verify()
space()
clearConsole()
space()
banner(value)
space()
print(Fore.LIGHTCYAN_EX + "Welcome to EnDa Calculator!")
print(Fore.LIGHTYELLOW_EX + "[TIP] >> For constants like pi or euler number enter the pi or euler!")
space()
while True:
    print(Fore.LIGHTRED_EX + "Please enter the number to continue!" + Fore.WHITE)
    first = input("First number : ")
    space()
    if str(first).lower() in ("pi"):
        first = pi
    elif str(first).lower() in ("e","euler"):
        first = euler
    try:
        float(first)
    except:
        print(Fore.RED + "[ERROR] >> Please enter a number!")
        space()
    else:
        first = int(first)
        limit_root = int(first ** (1/2))
        lists = []
        for i in range(1,limit_root + 1):
            f = 2 * i + 1
            result = f * i
            lists.append(result)
        the_result = sum(lists)
        
        x = f"Root of : [1] + ... + [{first}] = {the_result}"
        print(Fore.GREEN + f"Root of : [1] + ... + [{first}] = {the_result}")
        saveHistory(x)
        
    space()
    print(Fore.RED + "Do you want to do another calculation?")
    calculation = input("(Y)es or (N)o : ")
    space()
    if str(calculation).lower() in ("y","yes","(y)es","(y)"):
        pass
    else:
        print(Fore.BLUE + "Roger, thank you for using EnDa Calculator!" + Fore.RESET)
        time.sleep(2)
        exit()

#Powered by WBTER, EnDa Team in 2022
