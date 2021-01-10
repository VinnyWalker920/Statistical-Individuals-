import pprint
from math import ceil
from random import choice, randint, random
from statistics import mean
from scipy.stats import percentileofscore
import numpy as np
pp = pprint.PrettyPrinter(width=120, depth=25)

def GeneticCode():
    Code = []
    for i in range(20):
        strand = np.random.uniform(low=0.01, high=1.0, size=i + 1)
        # strand = np.random.randint(1, 100, size=i + 1)
        Code.append(strand)
    return Code

#For Actual analysis 'PredictorNumber' is irrelevant. Kept so Genetic AI works
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



