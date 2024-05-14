import numpy as np

class LinearLayer:
    def __init__(self, n_in, n_out, batch_size, activate=None, lr = 0.001):
        self.W = np.random.normal(size=(n_in, n_out))
        self.b = np.zero(size=(batch_size, n_out)) #可以通过将偏差初始化为0来很好地训练网络
        self.batch_size = batch_size
        self.activate = activate
        self.lr = lr

    def forward(self, x):
        self.x = x #x:(batch_size, n_in)
        output = np.dot(self.x, self.W) + self.b
        if self.activate == 'sigmoid':
            output = 1 / (1 + np.exp(-output))
        if self.activate == 'tanh':
            output = np.tanh(output)
        if self.activate == 'relu':
            output = np.maximum(0, output)
        self.activate_output = output
        return output

    def backward(self, y):
        # if self.activate == 'sigmoid':
        self.dW =





