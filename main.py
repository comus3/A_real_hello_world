import random
import string
import time
import copy
from os import system, name


def init(desired,max,d,c,casinoAmount,casinoDur):
    global delay
    global alphabet
    global desiredString
    global lettersMax
    global clear
    global casinoSystem
    casinoSystem = casinosystem(casinoDur,100-casinoAmount)
    clear = c
    delay = d
    lettersMax = max
    alphabet = string.ascii_letters
    alphabet = alphabet+"0123456789"
    desiredString = desired

def stringSwiper(actuPrint,dicoString):
    """
    output = ""
    first = list(dicoString.keys())[0]
    output = output + actuPrint[:first-1]+ dicoString[first][0]
    for key in dicoString:
        if key == first:
            continue
        output = output + actuPrint[len(output):key-1] + dicoString[key][0]
    return output
    """
    longueurActu = len(actuPrint)
    if longueurActu == 1:
        return actuPrint + dicoString[1]
    else:
        output = ""
        for index in range(longueurActu):
            if index not in dicoString:
                output = output + actuPrint[index]
            else:
                output = output + dicoString[index]
        if longueurActu in dicoString:
            output = output+dicoString[longueurActu]
        return output
    
def letter(lettre,actuPrint):
    if lettre not in alphabet and not(casinoSystem.isCasino(len(actuPrint))):
        actuPrint = actuPrint + lettre
        if clear:clearT()
        print(actuPrint)
        time.sleep(delay)
        return actuPrint
    elif not(casinoSystem.isCasino(len(actuPrint))):
        i = 0
        randChar = chr(32)
        while i<lettersMax and randChar != lettre:
            actuPrint = casinoSystem.activated(actuPrint)
            i = i + 1
            randChar = alphabet[random.randint(0,len(alphabet)-1)]
            actuPrint = actuPrint + randChar
            if clear:clearT()
            if randChar!=lettre:
                print(actuPrint)
                time.sleep(delay)
                actuPrint = actuPrint[:-1]
            else: return actuPrint
        if clear:clearT()
        actuPrint = actuPrint + lettre
        print(actuPrint)
    else:
        for _ in range(lettersMax):
            if clear:clearT
            actuPrint = casinoSystem.activated(actuPrint)
            print(actuPrint)
        if clear:clearT()
    time.sleep(delay)
    return actuPrint

class casinosystem():
    def __init__(self,duration,amt):
        self.duration = duration
        self.amt = amt
        self.casinoDico = {}
    def isCasino(self,index):
        return index in self.casinoDico
    def activated(self,actuPrint):
        return self.casinoLetters(actuPrint)
    def casinoNew(self,actuPrint,targetLetter):
        amtLeft = len(desiredString)-len(actuPrint)
        new = random.randint(0,100) > self.amt and amtLeft>2
        if new:
            index = len(actuPrint)
            if index not in self.casinoDico:self.casinoDico[index]=[targetLetter,self.duration]
    def casinoLetters(self,actuPrint):
        changesDico = {}
        dicoCache = copy.copy(self.casinoDico)
        for key in dicoCache:
            if self.casinoDico[key][1]==0:
                actuPrint = self.casinoStop(key,actuPrint)
            else:
                changesDico[key] = alphabet[random.randint(0,len(alphabet)-1)]
                self.casinoDico[key][1] = self.casinoDico[key][1] - 1
        if changesDico == {}:
            return actuPrint
        return stringSwiper(actuPrint,changesDico)
    def casinoStop(self,letterIndex,actuPrint):
        output = actuPrint[:letterIndex]+str(self.casinoDico[letterIndex][0])+actuPrint[letterIndex+1:]
        del self.casinoDico[letterIndex]
        return output

def clearT():
    # for windows
   if name == 'nt':
        _ = system('cls')
   # for mac and linux
   else:
        _ = system('clear')
    

def hackerPrint(string,max=3,d=0.01,clear=True,casinoAmount=0,casinoDur=1):
    init(string,max,d,clear,casinoAmount,casinoDur)
    actuPrint = ""
    while actuPrint != desiredString:
        longueur = len(actuPrint)
        if longueur!=len(desiredString):
            lettre = desiredString[longueur]
            if casinoAmount>0 and longueur>0:
                casinoSystem.casinoNew(actuPrint,lettre)
            actuPrint = letter(lettre,actuPrint)
        else:
            actuPrint = casinoSystem.activated(actuPrint)
            if clear:clearT
            print(actuPrint)
        
        


if __name__ == '__main__':
    hackerPrint('Hello World',3,0.01,True,100,5)