import pprint
from math import ceil
from random import choice, randint, random
from statistics import mean
from scipy.stats import percentileofscore
from util import MaxTupleClassSort, RemovePercent, GeneticCode, Crossover, Mutaion, SpecificTupleClassSort

pp = pprint.PrettyPrinter(width=120, depth=25)


class Member:
    def __init__(self):
        self.RawCode = GeneticCode()
        # Predictor Number Mean(Sigma X 1-20)
        self.PredictorNumber = self.RawCode[19][0]

    def SetCode(self, code):
        self.RawCode = code
        self.PredictorNumber = mean([i[0] for i in self.RawCode])
    def __repr__(self):
        return self.RawCode



class Environment:
    def __init__(self, startingSize, removalPorportion):
        self.porportion = removalPorportion
        self.Population = []
        self.Children = []
        self.Populate(startingSize)

    def __repr__(self):
        #TODO: make Percentile only show when it is MAX optimizing
        #TODO: make 'highestPredictedNumber' replaceable by
        sizeOfPopulation = len(self.Population)
        avgPredictedNumber = mean([i.PredictorNumber for i in self.Population])
        highestPredictedNumber = [i.PredictorNumber for i in self.Population]
        highestPredictedNumber.sort()
        highestPredictedNumber.reverse()
        AmmountOfOptimalValues = len([i.PredictorNumber for i in self.Population if i == 50])#TODO: Make Dynamic
        percentileOfOptimalValues = percentileofscore(sorted([i.PredictorNumber for i in self.Population]),80)
        str = f"Population Size: {sizeOfPopulation} \n"\
              f"Average Score: {avgPredictedNumber} \n" \
              f"Ammount Of Optimal Scores: {AmmountOfOptimalValues} \n" \
              # f"Highest Score: {highestPredictedNumber[0]}\n"\
              # f"Percentile of Most Optimal Score: {percentileOfOptimalValues}"
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

    def SortPopulation(self, OptToo='Max' ):
        if OptToo == 'Max':
            self.Population = MaxTupleClassSort(
                zip([i.PredictorNumber for i in self.Population], range(len(self.Population)), self.Population))
        else:
            self.Population = SpecificTupleClassSort(OptToo,
                zip([i.PredictorNumber for i in self.Population], self.Population))

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


#Genetic Algorithm Implementation V1
env = Environment(100, .65)
print("Starting Metrics: \n" + str(env) + "\n")
for epoch in range(500):
    children = []
    for i in range(ceil(len(env.Population)/2)):
        sup = choice(env.Population)
        inf = choice(env.Population)
        if inf is sup:
            pass
        for i in ProCreate(sup, inf):
            children.append(i)
    env.SortPopulation(OptToo=50)
    env.CropPopulation()
    env.AddChildren(children)
    env.MergeChildren()
    print("epoch " + str(epoch+1) + "/100000\n" + str(env) + "\n")

env.SortPopulation()
# pp.pprint([i.RawCode for i in env.Population])
