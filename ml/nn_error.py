import numpy as np

#input layer
X = np.array([[1,0,0], [0,1,0], [0,0,1]])
#output layer
y = np.array([[1], [1], [0]])

# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative sigmoid function
def derivative_sigmoid(x):
    return x * (1 - x)

# variable initialization
epoch = 50
lr = 0.1
inputlayer_neurons = X.shape[1]
hiddenlayer_neurons = 3
outputlayer_neurons = y.shape[1]

# weight and bias
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, outputlayer_neurons))
bout = np.random.uniform(size=(1, outputlayer_neurons))

# train
for i in range(epoch):
    # forward
    hidden_layer_input1 = np.dot(X, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hidden_layer_activate = sigmoid(hidden_layer_input)
    output_layer_input1 = np.dot(hidden_layer_activate, wout)
    output_layer_input = hidden_layer_input1 + bout
    output = sigmoid(output_layer_input)

    # backforward
    import pdb
    pdb.set_trace()
    E = y - output
    slope_output_layer = derivative_sigmoid(output) # p(1-p)
    slope_hidden_layer = derivative_sigmoid(hidden_layer_activate)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hidden_layer_activate.T.dot(d_output) * lr
    bout += np.sum(d_output, axis= 0, keepdims= True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis= 0, keepdims=True) * lr

print('actual : \n%s' % y)
print('predicted: \n', output)