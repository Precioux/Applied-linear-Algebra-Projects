import numpy as np
from Calc import Calculator


def makeMatrix():
    j = 0
    for element in elements:
        x = []
        for compound in ingredients:
            flag = False
            i = 0
            for c in compound:
                if c == element:
                    flag = True
                    n = len(compound)
                    if i + 1 < n:
                        if 65 <= ord(compound[i + 1]) <= 90:
                            arr = [1]
                            x = x + arr
                        else:
                            arrI = [int(compound[i + 1])]
                            x = x + arrI
                    else:
                        arr = [1]
                        x = x + arr
                i += 1
            if flag == False:
                arrZ = [0]
                x = x + arrZ

        for compound in products:
            flag = False
            i = 0
            for c in compound:
                if c == element:
                    flag = True
                    n = len(compound)
                    if i + 1 < n:
                        if 65 <= ord(compound[i + 1]) <= 90:
                            arr = [-1]
                            x = x + arr
                        else:
                            k = int(compound[i + 1])
                            k = k * -1
                            arrI = [k]
                            x = x + arrI
                    else:
                        arr = [-1]
                        x = x + arr

                i += 1
            if not flag:
                arrZ = [0]
                x = x + arrZ

        arrf = [0]
        x = x + arrf
        j += 1
        X.append(x)


elements = input("Enter elements: ")
equation = input("Enter equation: (example: 𝐶2𝐻6+𝑂2>𝐶𝑂2+𝐻2𝑂")
data = equation.split(">")
ingredients = data[0].split("+")
products = data[1].split("+")

shape = (len(elements), len(ingredients) + len(products))
X = []
makeMatrix()
obj = Calculator(X, len(elements), len(ingredients) + len(products))
obj.ready()
