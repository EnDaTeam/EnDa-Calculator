#The EnDa Calculator's Math Functions

#Import needed modules
from colorama import Fore
import time

#Define needed math functions
def add(x,y):
    print(Fore.GREEN + f"{x} + {y} = {x + y}" + Fore.WHITE)
    return f"{x} + {y} = {x + y}"

def subtract(x,y):
    print(Fore.GREEN + f"{x} - {y} = {x - y}" + Fore.WHITE)
    return f"{x} - {y} = {x - y}"

def multiply(x,y):
    print(Fore.GREEN + f"{x} * {y} = {x * y}" + Fore.WHITE)
    return f"{x} * {y} = {x * y}"

def divide(x,y):
    print(Fore.GREEN + f"{x} / {y} = {x / y}" + Fore.WHITE)
    return f"{x} / {y} = {x / y}"

def divide_nd(x,y):
    print(Fore.GREEN + f"{x} // {y} = {x // y} rest {x % y}" + Fore.WHITE)
    return f"{x} // {y} = {x // y} rest {x % y}"

def power(x,y):
    print(Fore.GREEN + f"{x} ** {y} = {x ** y}" + Fore.WHITE)
    return f"{x} ** {y} = {x ** y}"

def root(x,y):
    print(Fore.GREEN + f"{y} root of {x} = {x ** (1/y)}" + Fore.WHITE)
    return f"{y} root of {x} = {x ** (1/y)}"

if __name__ == "__main__":
    time1 = time.time()
    add(1,2)
    subtract(1,2)
    multiply(1,2)
    divide(1,2)
    divide_nd(1,2)
    power(1,2)
    root(1,2)
    time2 = time.time()
    print(f"All process finished in {time2 - time1} seconds")

#Powered by WBTER, EnDa Team in 2022