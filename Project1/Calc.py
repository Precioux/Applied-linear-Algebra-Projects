import numpy as np


class Calculator:
    def __init__(self, matrix, elements):
        self.matrix = np.array(matrix)
        self.matrix = self.matrix.astype(float)
        self.elements = elements
        self.check = np.array(False)
        l = 1
        while l < self.elements:
            self.check = np.append(self.check, False, axis=None)
            l += 1

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
        # print(f"pivot found for{k} is {i}")
        return i

    def changeRow(self, i, e):
        if i != e and self.check[i] == False:
            temp = np.array(self.matrix[e])
            self.matrix[e] = self.matrix[i]
            self.matrix[i] = temp
        #   print(f"i= {i} => ", self.matrix[i])
        #  print("temp : ", temp)
        # print("result of changing rows: ")
        self.check[e] = True
        # self.printer()

    def setOne(self, e):
        a = int(self.matrix[e][e])
        if a != 0:
            #  print("a is", a)
            tmp = self.matrix[e] / a
            self.matrix[e] = tmp
        #  print("result of divition: ")
        # print(self.matrix)

    def setZero(self, e):

        if e + 1 < self.elements:
            c = e + 1
            while c < self.elements:
                #  print(f"set to zero for {e} applied on {c}")
                #  print(self.matrix[c][e])
                n = int(self.matrix[c][e])
                self.matrix[c] = self.matrix[c] - self.matrix[e] * n
                self.setOne(c)
                c += 1

    def makeEchlon(self):
        e = 0
        while e < self.elements:
            #  print(f"for e={e}")
            i = self.findPivot(e)
            self.changeRow(i, e)
            self.setOne(e)
            e += 1
        k = 0
        while k < self.elements:
            self.setZero(k)
            k += 1

    def reduceIt(self):
        t = 0
        while t < self.elements:
            for i in range(0, 3):
                n = float(self.matrix[t][i])
                if n != 0 and t != i:
                    self.matrix[t] = self.matrix[t] - n * self.matrix[i]
            t += 1

    def getResults(self):
            s=0
            while s<self.elements:
                print(f"X{s} = {self.matrix[s][3]}")
                s+=1

    def ready(self):
        self.printer()
        self.makeEchlon()
        print("Echlon Matrix:")
        self.printer()
        self.reduceIt()
        print("Reduced Echlon Matrix:")
        self.printer()
        print("Results:")
        self.getResults()
