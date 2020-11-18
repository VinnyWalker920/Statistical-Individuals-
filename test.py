from itertools import zip_longest
x = [1,2,3,4,5,6,7,8,9]
y = [3,6,4,7,3,8,1,4,6]


class obj:
	def __init__(self, num):
		self.num = num

t = [obj(i) for i in range(len(x))]

X = list(zip(x,t))

def SpecificTupleClassSort(num, TupleList):
    Greater = [i for i in TupleList if i[0] > num]
    Equal = [i for i in TupleList if i[0] == num]
    Lesser = sorted([i for i in TupleList if i[0] < num], reverse=True)
    Zipper = list(zip_longest(Greater, Lesser, fillvalue="x"))#[((val,obj),(val,obj)),((val,obj),(val,obj))...]
    SortedTuples = Equal + [item for obj in Zipper for item in obj if item is not "x"]
    # return [i for x, i in SortedTuples]
    return SortedTuples

print(SpecificTupleClassSort(5, X))

# print(list(yes + no))


