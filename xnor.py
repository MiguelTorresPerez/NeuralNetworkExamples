import math
import numpy as np

#logic gate xnor cnn approach

##funct
sigmoid = lambda n : 1 / (1 + math.pow(math.e,-n))
forwardP = lambda x, theta : [sigmoid(np.dot([1]+x,t)) for t in theta]



x1 , x2 = input()
inputF = [float(x1),float(x2)]

#theta vectors of each layer
thetaMatrixOutputLayer = [[-10,20,20]]
thetaMatrixHiddenLayer = [[-30,20,20],[10,-20,-20]]

a2 = forwardP(inputF,thetaMatrixHiddenLayer)
H0 = forwardP(a2,thetaMatrixOr)
print(H0)
