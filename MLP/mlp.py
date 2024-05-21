import numpy as np


# Sigmoid激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


# 交叉熵损失函数及其导数
def cross_entropy(output, y_target):
    return -np.mean(y_target * np.log(output) + (1 - y_target) * np.log(1 - output))


def cross_entropy_derivative(output, y_target):
    return -(y_target / output - (1 - y_target) / (1 - output))

# MSE损失函数及其导数
def mse(output, y_target):
    return np.mean(np.square(output - y_target))

def mse_derivative(output, y_target):
    return 2 * (output - y_target)

# MLP类
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        # 权重初始化
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def forward(self, X):
        # 前向传播
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    # 反向传播
    def backward(self, X, y, output, learning_rate):
        # 损失函数梯度
        # loss_grad = cross_entropy_derivative(output, y)
        loss_grad = mse_derivative(output, y)

        # 输出层梯度
        a2_grad = loss_grad * sigmoid_derivative(self.a2)
        # 计算隐藏层到输出层的权重的梯度
        W2_grad = np.dot(self.a1.T, a2_grad)
        # 计算输出层的偏置的梯度
        b2_grad = np.sum(a2_grad, axis=0, keepdims=True) # axis=0表示沿着第一个轴（列方向）进行求和；keepdims=True，那么求和后的数组会保持原来的维度，但是被求和的轴的长度会变成1，keepdims=False（默认值），那么求和后的数组会减少一个维度。

        # 计算隐藏层的梯度
        a1_grad = np.dot(a2_grad, self.W2.T) * sigmoid_derivative(self.a1) # 链式法则
        # 计算输入层到隐藏层的权重的梯度
        W1_grad = np.dot(X.T, a1_grad)
        # 计算隐藏层的偏置的梯度
        b1_grad = np.sum(a1_grad, axis=0)

        # 使用学习率更新参数
        self.W1 -= learning_rate * W1_grad
        self.b1 -= learning_rate * b1_grad
        self.W2 -= learning_rate * W2_grad
        self.b2 -= learning_rate * b2_grad

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # 前向传播
            output = self.forward(X)
            # 计算损失
            loss = cross_entropy(output, y)
            # 反向传播
            # import pdb;pdb.set_trace()
            self.backward(X, y, output, learning_rate)
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")


# 创建网络
mlp = MLP(input_size=2, hidden_size=5, output_size=1)

# 训练数据
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# 训练网络
mlp.train(X, y, epochs=1000, learning_rate=0.1)
