from random import randint
from statistics import mean

def generateDNA(*Kwargs):
    DNA = []
    for x,i in enumerate(range(20)):
        DNA.append(randomList(x+1))
    return DNA

def randomList(length):
    RandomList = []
    for i in range(length):
        RandomList.append(randint(1,99))
    return RandomList

class Member():
    def __init__(self,DNA,Type):
        self.DNA = DNA
        self.Gender = self.evaluateGender()
        self.Life = self.evaluateLife()
    
    def evaluateGender(self):
    	determinate = round(mean(self.DNA["L"]))
    	if determinate%2 is not 0:
    		return 2
    	else: 
    		return 1
    
    def evaluateLife(self):
    	Life = round(mean(self.DNA["D"]))
    	return Life