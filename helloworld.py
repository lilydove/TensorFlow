import tensorflow as tf

# Create a constant
hello = tf.constant('Hello,World!')
# Create a session
sess = tf.Session()
# Execute
result = sess.run(hello)
# Close the session
sess.close()
# Output
print(result)
