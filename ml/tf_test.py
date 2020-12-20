import tensorflow as tf

def add_layer(input, input_size, output_size):
    # input = tf.Variable(tf.random([3,1]))
    # hidden = tf.Variable(tf.random(5,1))
    # output = tf.Variable(tf.random(2,1))
    Ws = tf.Variable(tf.random([input_size, output_size]))
    bs = tf.Variable(tf.random([1, output_size]))
    ws_b = tf.matmul(input, Ws) + bs
    output = tf.nn.relu(ws_b)
    return output
x = tf.placeholder([None, 3]) # todo
y = tf.placeholder([None, 2]) # todo
x_data = None
y_data = None
hidden_l = add_layer(x, 3, 5)
output_l = add_layer(hidden_l, 5, 2)

loss = tf.reduce_mean(tf.square(output_l - y))
train = tf.train.AdamOptimizer(0.01).minimize(loss)

with tf.session() as sess:
    sess.run(train, feed_dict = {x: x_data, y:y_data})
