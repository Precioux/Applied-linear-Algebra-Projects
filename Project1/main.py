import numpy as np
X=[]
def makeMatrix():
    for element in elements:
        print("seraching for "+element)
        x=[]
        j=0
        for compound in ingredients:
            print("ing:")
            print(compound)
            for c in compound:
                print(c)
                i=0
                if(c==element):
                    print("YES")
              #      x[j]=int(compound[i+1])
                i+=1
        for compound in products:
            print("pro\n")
            print(compound)
            for c in compound:
                print(c)
                i = 0
                if (c == element):
                    print("YES")
              #      x[j] = int(compound[i + 1])
                i+=1
        j+=1
       # X.append(x)
        #print(X)

elements=input("Enter elements: ")
equation=input("Enter equation: (example: 𝐶2𝐻6+𝑂2→𝐶𝑂2+𝐻2𝑂)")
data=equation.split("→")
ingredients=data[0].split("+")
products=data[1].split("+")
print(ingredients)
print(products)
shape=(len(elements),len(ingredients)+len(products))
makeMatrix()
