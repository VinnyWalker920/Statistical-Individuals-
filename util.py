from math import ceil
from random import randint
from statistics import mean
import numpy.random as np
from functools import reduce
import operator



def GeneticCode():
    Code = []
    for i in range(20):
        strand = np.randint(100, size=i + 1)
        Code.append(strand)
    return Code


def TupleClassSort(TupleList):
    listObject = list(TupleList)
    listObject.sort()
    listObject.reverse()
    return [i for x, _, i in listObject]


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
        x[randint(0, len(x) - 1)] = randint(mean(i), 100)
        finalCode.append(x)
    return finalCode

def prod(x):
    return reduce(operator.mul,x,1)




# #MAXIMUM CASE
# lk = []
# for i in range(20):
#     code = []
#     for i in range(i+1):
#         code.append(100)
#     lk.append(code)
# print(mean([sum(i) for i in lk]))

# cap = [[82],
#        [88, 42],
#        [46, 37, 56],
#        [69, 46, 72, 19],
#        [37, 86, 32, 95, 26],
#        [15, 81, 77, 31, 69, 71],
#        [23, 49, 86, 23, 28, 90, 3],
#        [79, 54, 70, 40, 3, 2, 93, 55],
#        [7, 57, 28, 42, 7, 65, 35, 36, 28],
#        [96, 85, 60, 46, 45, 15, 74, 94, 75, 9],
#        [29, 19, 95, 14, 49, 84, 23, 34, 8, 27, 22],
#        [58, 72, 21, 18, 58, 77, 22, 90, 46, 72, 95, 82],
#        [72, 20, 85, 47, 4, 26, 35, 64, 88, 29, 80, 47, 39],
#        [80, 66, 51, 82, 44, 49, 73, 66, 77, 1, 35, 78, 68, 97],
#        [35, 59, 29, 5, 53, 81, 88, 98, 22, 32, 23, 41, 64, 43, 25],
#        [51, 9, 6, 84, 4, 44, 38, 46, 46, 71, 58, 41, 21, 14, 76, 71],
#        [18, 87, 12, 57, 91, 55, 81, 97, 82, 86, 97, 65, 72, 57, 83, 9, 29],
#        [84, 91, 27, 42, 42, 69, 9, 19, 66, 52, 92, 10, 80, 3, 51, 45, 66, 90],
#        [93, 13, 96, 82, 36, 57, 2, 69, 86, 68, 74, 13, 58, 47, 95, 77, 32, 64, 76],
#        [9, 40, 22, 99, 13, 44, 44, 17, 18, 44, 16, 41, 44, 41, 90, 77, 89, 80, 30, 41]]
#
# tin = [[10],
#        [91, 67],
#        [13, 11, 40],
#        [72, 97, 22, 85],
#        [22, 83, 32, 74, 52],
#        [44, 80, 47, 28, 18, 71],
#        [77, 97, 34, 39, 52, 15, 69],
#        [8, 82, 48, 96, 66, 83, 93, 56],
#        [50, 49, 58, 50, 62, 73, 95, 53, 74],
#        [44, 45, 76, 56, 15, 58, 36, 3, 50, 83],
#        [100, 80, 99, 95, 26, 7, 96, 2, 84, 19, 84],
#        [60, 81, 73, 34, 83, 36, 45, 3, 18, 76, 38, 11],
#        [75, 11, 61, 6, 53, 86, 68, 53, 86, 2, 37, 70, 24],
#        [68, 29, 91, 54, 79, 76, 22, 76, 80, 70, 96, 61, 74, 9],
#        [72, 97, 9, 59, 1, 84, 70, 10, 32, 44, 91, 39, 50, 7, 40],
#        [3, 11, 35, 95, 61, 14, 79, 48, 64, 56, 62, 22, 21, 21, 80, 59],
#        [65, 20, 5, 39, 23, 9, 88, 43, 8, 7, 86, 99, 44, 34, 96, 20, 3],
#        [78, 68, 60, 14, 13, 38, 22, 32, 30, 31, 58, 55, 32, 2, 84, 40, 82, 31],
#        [2, 35, 77, 32, 25, 61, 67, 93, 68, 93, 84, 31, 26, 35, 36, 97, 26, 8, 15],
#        [13, 15, 30, 12, 66, 10, 80, 6, 71, 73, 27, 71, 41, 34, 66, 79, 80, 75, 27, 77]]
