import pprint
from math import ceil
from random import choice, randint
from statistics import mean
from util import TupleClassSort, RemovePercent, GeneticCode, Crossover, Mutaion, prod

pp = pprint.PrettyPrinter(width=120, depth=25)


class Member:
    def __init__(self):
        self.RawCode = GeneticCode()
        # Predictor Number Mean(Sigma X 1-20)
        self.PredictorNumber = mean([sum(i) for i in self.RawCode])

    def SetCode(self, code):
        self.RawCode = code
        self.PredictorNumber = mean([sum(i) for i in self.RawCode])
    def __repr__(self):
        return self.RawCode



class Environment:
    def __init__(self, startingSize, removalPorportion):
        self.porportion = removalPorportion
        self.Population = []
        self.Children = []
        self.Populate(startingSize)

    def __repr__(self):
        sizeOfPopulation = len(self.Population)
        avgPredictedNumber = mean([i.PredictorNumber for i in self.Population])
        highestPredictedNumber = [i.PredictorNumber for i in self.Population]
        highestPredictedNumber.sort()
        highestPredictedNumber.reverse()
        str = f"Population Size: {sizeOfPopulation} \n"\
              f"Average Score: {avgPredictedNumber} \n"\
              f"Highest Score: {highestPredictedNumber[0]}"
        return str

    def Populate(self, startingSize):
        for i in range(startingSize):
            c = Member()
            self.Population.append(c)

    def AddChildren(self, children):
        self.Children += children

    def MergeChildren(self):
        for i in self.Children:
            self.Population.append(i)
        self.Children = []

    def SortPopulation(self):
        self.Population = TupleClassSort(
            zip([i.PredictorNumber for i in self.Population], range(len(self.Population)), self.Population))

    def CropPopulation(self):
        self.Population = RemovePercent(self.Population, self.porportion)

def ProCreate(dom, sub):
    children = []
    birthrate = choice([1, 2])
    M = dom.RawCode
    F = sub.RawCode
    CrossoverCode = Crossover(M, F)
    for i in range(birthrate):
        c = Member()
        c.SetCode(Mutaion(CrossoverCode))
        children.append(c)

    return children


#Genetic Algorthim Implementaion V1
env = Environment(50, .20)
print("Starting Metrics: \n" + str(env) + "\n")
for epoch in range(10):
    children = []
    for i in range(ceil(len(env.Population)/2)):
        sup = choice(env.Population)
        inf = choice(env.Population)
        if inf is sup:
            pass
        for i in ProCreate(sup, inf):
            children.append(i)
    env.SortPopulation()
    env.CropPopulation()
    env.AddChildren(children)
    env.MergeChildren()
    print("epoch " + str(epoch+1) + "/100\n" + str(env) + "\n")

# pp.pprint([i.RawCode for i in env.Population])
