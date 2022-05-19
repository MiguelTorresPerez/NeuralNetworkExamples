

##### Neural networks with sigmoid activation function

The activation value of each unit (node or neuron) is calculated 
computing the dot product of the theta parameter matrix transposed and the feature matrix.

![expansion](http://www.sciweavers.org/upload/Tex2Img_1652986141/eqn.png)

Then we apply the sigmoid function to each element to obtain the matrix of the activation units in layer l.

![actMatrix](http://www.sciweavers.org/upload/Tex2Img_1652895306/eqn.png)








#### 1. And Gate (and.py)

  The neural network is composed of
<ul> 
<li>1 input layer with 3 units one of them the bias (x0==1)</li>
<li>1 output layer with 1 unit</li>
</ul>

The theta matrix [-30,20,20] of weights is picked arbitrarily so the sigmoid function will map each parameter


#### 1. Xnor Gate (xnor.py)

  The neural network is composed of
<ul> 
<li>1 input layer with 3 units one of them the bias (x0==1)</li>
<li>1 hidden layer with 3 units one of them the bias </li>
<li>1 output layer with 1 unit</li>
</ul>

( x1 and x2 ) or ( (not x1) and (not x2) ) = XNOR
