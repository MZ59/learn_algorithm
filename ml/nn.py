import numpy as np
import sklearn
import matplotlib
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

#生成平面点分布
np.random.seed(0)
X, y = make_moons(200, noise= 0.20)
plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
plt.show()
print(X[1])
print(y[19])

#决策边界
def plot_decision_boundary(pred_func):
    # 最值
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

# from sklearn.linear_model import LogisticRegressionCV
# clf = LogisticRegressionCV(cv=4)
# clf.fit(X, y)
# plot_decision_boundary(lambda x: clf.predict(x))
# plt.title('Logistic Regression')
# plt.show()

num_examples = len(X)
nn_input_dim = 2
nn_output_dim = 2

#梯度下降参数
epsilon = 0.001
reg_lambda = 0.01


X = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]) #X: 4*3
y = np.array([[1], [1], [1], [0]]) #y:4*2
input_layer_neu = X.shape[1]
hidden_layer_neu = 4
output_layer_neu = y.shape[1]
w1 = np.random.uniform(size=(input_layer_neu, hidden_layer_neu))
b1 = np.random.uniform(size=(1, hidden_layer_neu))
w2 = np.random.uniform(size=(hidden_layer_neu, output_layer_neu))
b2 = np.random.uniform(size=(1, output_layer_neu))
import pdb;pdb.set_trace()
z1 = X.dot(w1) + b1  # z1: 4*4
a1 = np.tanh(z1)  # tanh激活
z2 = a1.dot(w2) + b2  # z2: 200*2




#损失函数, 交叉熵
def calcualte_loss(model):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    '''
        W1: 2*3
        b1: 1*3
        W2: 3*2
        b2: 1*2
    '''
    # 前向传播
    z1 = X.dot(W1) + b1  # z1: 200*3
    a1 = np.tanh(z1)  # tanh激活
    z2 = a1.dot(W2) + b2  # z2: 200*2


