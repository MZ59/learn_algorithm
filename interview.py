import tensorflow as tf

def add_layer(input, input_size, output_size, active_function=None):
    weight = tf.Variable(tf.random_normal_initializer([input_size, output_size]))
    bias = tf.Variable(tf.random_normal_initializer([1, output_size]))
    wx_b = tf.matmul(input, weight) + bias
    if active_function:
        output = active_function(wx_b)
    else:
        output = wx_b
    return output

xs = tf.placeholder(tf.float32, [None, 10])
ys = tf.placeholder(tf.float32, [None, 1])

hidden_layer = add_layer(xs, 10, 15, tf.nn.relu)
pred = add_layer(hidden_layer, 15, 1, None)

#损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - pred), reduction_indices= [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

x = None
y = None

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(100):
    sess.run(train_step, feed_dict={xs : x, ys : y})
sess.close()


