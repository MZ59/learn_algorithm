import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    exp_z = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def cross_entropy_loss(y_true, y_pred):
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))

class MLP:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.zeros(hidden_dim)
        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.zeros(output_dim)

    def forward(self, x):
        self.z1 = np.dot(x, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        y_pred = softmax(self.z2)
        return y_pred

    def backward(self, x, y_true, y_pred, learning_rate):
        N = x.shape[0]
        dZ2 = y_pred - y_true
        dW2 = np.dot(self.a1.T, dZ2) / N
        db2 = np.sum(dZ2, axis=0) / N
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * (self.a1 * (1 - self.a1))
        dW1 = np.dot(x.T, dZ1) / N
        db1 = np.sum(dZ1, axis=0) / N

        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1

    def train(self, x, y, epochs, learning_rate):
        for epoch in range(epochs):
            y_pred = mlp.forward(x)
            loss = cross_entropy_loss(y, y_pred)
            mlp.backward(x, y, y_pred, learning_rate)
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss {loss}")


# 示例用法
input_dim = 4
hidden_dim = 6
output_dim = 3
mlp = MLP(input_dim, hidden_dim, output_dim)

x = np.random.randn(5, input_dim)
y_true = np.eye(output_dim)[np.random.randint(0, output_dim, 5)]

import pdb;pdb.set_trace()
mlp.train(x, y_true, 1000, 0.1)
# y_pred = mlp.forward(x)
# loss = cross_entropy_loss(y_true, y_pred)
# mlp.backward(x, y_true, y_pred, 0.1)