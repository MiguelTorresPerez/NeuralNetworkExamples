
import math
import numpy as np

sigmoid = lambda n : 1 / (1 + math.pow(math.e,-n))

#logic gate cnn approach
x1 , x2 = input()

#and theta matrix
thetaMatrix = [-30,20,20]

#variable vector with bias unit == 1
v = [1,float(x1),float(x2)]


H0 = sigmoid(np.dot(thetaMatrix,v))
