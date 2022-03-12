import numpy as np


class Calculator:
    def __init__(self, matrix, elements):
        self.matrix = matrix
        self.elements = elements

    def printer(self):
        print(self.matrix)

    def findPivot(self, k):
        i = 0
        flag = False
        while flag == False:
            if self.matrix[i][k] != 0:
                flag = True
            else:
                i += 1
        return i

    def changeRow(self, i, e):
        if i != e:
            tmp = self.matrix[e]
            self.matrix[e] = self.matrix[i]
            self.matrix[i] = tmp
        self.printer()

    def setZero(self, e):
        a = int(self.matrix[e][e])
        mx=np.array(self.matrix)
        if a!=0:
            print("a is",a)
            tmp=mx[e] / a
            mx[e]=tmp
            print("result: ")
            print(mx)



    def makeEchlon(self):
        e = 0
        while e < self.elements:
            i = self.findPivot(e)
            self.changeRow(i, e)
            self.setZero(e)
            e += 1
