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
    print(Fore.LIGHTRED_EX + "Please enter the first number to continue!" + Fore.WHITE)
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
        count = 1
        count2 = 1
        while count:
            print(Fore.LIGHTRED_EX + "Enter the operation from list")
            space()
            options()
            Fore.WHITE
            space()
            operation = input(Fore.WHITE + "Option : ")
            space()
            if str(operation) not in ("1","2","3","4","5","6"):
                print(Fore.RED + "[ERROR] >> Please enter an operation from list!")
                space()
            else:
                count = 0
                while count2:
                    print(Fore.LIGHTRED_EX + "Please enter the second number to continue!" + Fore.WHITE)
                    second = input("Second number : ")
                    if str(second).lower() in ("pi"):
                        second = pi
                    elif str(second).lower() in ("e","euler"):
                        second = euler
                    space()
                    try:
                        float(second)
                    except:
                        print(Fore.RED + "[ERROR] >> Please enter a number!")
                        space()
                    else:
                        first = float(first)
                        second = float(second)
                        count2 = 0
                        if operation == "1":
                            saveHistory(add(first,second))
                        elif operation == "2":
                            saveHistory(subtract(first,second))
                        elif operation == "3":
                            saveHistory(multiply(first,second))
                        elif operation == "4":
                            if first % second == 0:
                                saveHistory(divide(first,second))
                            else:
                                saveHistory(divide(first,second))
                                saveHistory(divide_nd(first,second))
                        elif operation == "5":
                            saveHistory(power(first,second))
                        elif operation == "6":
                            saveHistory(root(first,second))
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