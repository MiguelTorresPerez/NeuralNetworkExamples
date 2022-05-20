import math
import numpy as np



sigmoid = lambda n : 1 / (1 + math.pow(math.e,-n))
propagate = lambda x, theta : [sigmoid(np.dot([1]+x,t)) for t in theta]

'''Forward propagation from input layer to hypotheses H0 '''
def forwardP(input_matrix,layer_matrix):
    H0 = []
    for l in layer_matrix:
        H0 = propagate(input_matrix,l) if not H0 else propagate(H0,l)
        
    return H0

#matrix with all layer weights
matrix = [[[-30,20,20],[10,-20,-20]],[[-10,20,20]]]
x1 , x2 = input()
inputFeatures = [float(x1),float(x2)]

print(forwardP(inputFeatures,matrix))
