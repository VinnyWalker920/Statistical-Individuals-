import pprint

from statistics import mean
from util import *

pp = pprint.PrettyPrinter(width=100)


class Member:
    def __init__(self):
        self.RawCode = GeneticCode()
        # Predictor Number Mean(Sigma X 1-20)
        self.PredictorNumber = mean([sum(i) for i in self.RawCode])

    def SetCode(self, code):
        self.RawCode = code


class Env:
    def __init__(self, startingSize, removalPorportion):
        self.porportion = removalPorportion
        self.Population = []
        self.Children = []
        self.Populate(startingSize)

    def __str__(self):
        avgPredictedNumber = mean([i.PredictorNumber for i in self.Population])
        highestPredictedNumber = [i.PredictorNumber for i in self.Population].sort()[0]
        str = f"Average Score: {avgPredictedNumber} \n Highest Score: {highestPredictedNumber}"

    def Populate(self, startingSize):
        for i in range(startingSize):
            c = Member()
            self.Population.append(c)

    def AddChildren(self, children):
        self.children += children

    def MergeChildren(self):
        self.Population += self.Children

    def SortPopulation(self):
        self.Population = TupleClassSort(
            zip([i.PredictorNumber for i in self.Population], range(len(self.Population)), self.Population))

    def CropPopulation(self):
        self.Population = RemovePercent(self.Population, self.porportion)
