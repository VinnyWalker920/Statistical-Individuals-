from itertools import zip_longest
from math import ceil
from random import randint, choice
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import percentileofscore
from sklearn.metrics import r2_score


from subject import Member
from scipy.optimize import curve_fit


def MaxTupleClassSort(TupleList):
    listObject = list(TupleList)
    listObject.sort()
    listObject.reverse()
    return [i for x, _, i in listObject]

def SpecificTupleClassSort(num, TupleList):
    Greater = [i for i in TupleList if i[0] >= num]
    Lesser = sorted([i for i in TupleList if i[0] < num], reverse=True)
    Zipper = list(zip_longest(Greater, Lesser, fillvalue="x"))#[((val,obj),(val,obj)),((val,obj),(val,obj))...]
    SortedTuples = [item for obj in Zipper for item in obj if item is not "x"]
    return [i for x, i in SortedTuples]


def RemovePercent(listobj, porportion):
    NumberRemoved = ceil(porportion * len(listobj))
    return listobj[0:(-1 * NumberRemoved)]


def Crossover(a, b):
    newCode = []
    for i in range(20):
        if i % 2 == 0:  # even
            newCode.append(a[i])
        else:  # odd
            newCode.append(b[i])
    return newCode


def Mutaion(code):
    finalCode = []
    for i in code:
        x = i.copy()
        x[randint(0, len(x) - 1)] = np.random.randint(1, 100)
        # x[randint(0, len(x) - 1)] = np.random.uniform(low=0.01, high=1.0)
        finalCode.append(x)
    return finalCode

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
        avgPredictedNumber = np.mean([i.PredictorNumber for i in self.Population])
        highestPredictedNumber = [i.PredictorNumber for i in self.Population]
        highestPredictedNumber.sort()
        highestPredictedNumber.reverse()
        AmmountOfOptimalValues = len([i.PredictorNumber for i in self.Population if i == 50])#TODO: Make Dynamic
        percentileOfOptimalValues = percentileofscore(sorted([i.PredictorNumber for i in self.Population]),90)
        str = f"Population Size: {sizeOfPopulation} \n"\
              f"Average Score: {avgPredictedNumber} \n" \
              f"Highest Score: {highestPredictedNumber[0]}\n"\
              f"Percentile of Most Optimal Score: {percentileOfOptimalValues}"
              # f"Ammount Of Optimal Scores: {AmmountOfOptimalValues} \n" \
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

y_vals = []

#Genetic Algorithm Implementation V1
env = Environment(100, .75)
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
    env.SortPopulation(OptToo="Max")
    env.CropPopulation()
    env.AddChildren(children)
    env.MergeChildren()
    y_vals.append(len(env.Population))
    print("epoch " + str(epoch+1) + "/500\n" + str(env) + "\n")

env.SortPopulation()




x_vals= range(0,len(y_vals))
plt.scatter(x_vals,y_vals)
plt.ylabel("# of Cells")
plt.xlabel("Time(t) in Generations")
#
# mymodel1 = np.poly1d(np.polyfit(x_vals, y_vals, 10))
# mymodel2 = np.poly1d(np.polyfit(x_vals, y_vals, 5))
# mymodel3 = np.poly1d(np.polyfit(x_vals, y_vals, 3))

myline = np.linspace(0, 500, 1000000)


# plt.plot(myline, mymodel1(myline))
# plt.plot(myline, mymodel2(myline))
# plt.plot(myline, mymodel3(myline))
# print("r^2 ", r2_score(y_vals, mymodel1(x_vals)))
# print("r^2 ", r2_score(y_vals, mymodel2(x_vals)))
# print("r^2 ", r2_score(y_vals, mymodel3(x_vals)))

best_degree= []
for i in range(1,10):
    m = np.poly1d(np.polyfit(x_vals, y_vals, i))
    best_degree.append(r2_score(y_vals, m(x_vals)))

bd = best_degree.index(max(best_degree)) - 1

coeff = np.polyfit(x_vals, y_vals, bd)
print(coeff)
mymodel = np.poly1d(coeff)

plt.plot(myline, mymodel(myline))
print(bd)
print("r^2 ", r2_score(y_vals, mymodel(x_vals)))

plt.show()





