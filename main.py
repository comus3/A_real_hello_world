import random
import string
import time
from os import system, name


def init(desired,max,d,c):
    global delay
    global alphabet
    global desiredString
    global lettersMax
    global clear
    clear = c
    delay = d
    lettersMax = max
    alphabet = string.ascii_letters
    alphabet = alphabet+"0123456789"
    desiredString = desired

def letter(lettre,actuPrint):
    i = 0
    randChar = chr(32)
    while i<lettersMax and randChar != lettre:
        i = i + 1
        randChar = alphabet[random.randint(0,len(alphabet)-1)]
        actuPrint = actuPrint + randChar
        print(actuPrint)
        if randChar!=lettre:actuPrint = actuPrint[:-1]
        else: return actuPrint
    actuPrint = actuPrint + lettre
    print(actuPrint)
    return actuPrint

def clearT():
    # for windows
   if name == 'nt':
        _ = system('cls')
   # for mac and linux
   else:
        _ = system('clear')
    

def hackerPrint(string,max,d,clear):
    init(string,max,d,clear)
    actuPrint = ""
    while actuPrint != desiredString:
        if clear:clearT()
        lettre = desiredString[len(actuPrint)]
        actuPrint = letter(lettre,actuPrint)
        time.sleep(1)
        


if __name__ == '__main__':
    hackerPrint('Hello World',10,1,False)
    
    






    
    